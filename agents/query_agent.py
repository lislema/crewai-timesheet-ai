from openai import OpenAI
import os

class QueryAgent:
    def __init__(self):
        self.client = OpenAI()
        self.model = "gpt-3.5-turbo"

    def run(self, anomalies: list):
        print("[QueryAgent] Sending anomalies to OpenAI for summary...")
        chunks = self.chunk_list(anomalies)
        full_summary = ""

        for i, chunk in enumerate(chunks):
            print(f"[QueryAgent] Processing chunk {i+1}...")

            prompt = f"""Summarize the following timesheet anomalies in a helpful, professional way:
                        - Over 9 hours/day: may indicate overwork.
                        - Under 9 hours/day: may suggest incomplete shifts.
                        - Long lunches: could violate policy (>2h).
                        - Vacation or Sick Leave: legitimate but worth tracking.

                    """ + "\n".join(chunk)

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful HR assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3
            )

            full_summary += response.choices[0].message.content + "\n"

        return full_summary.strip()

    def chunk_list(self, items, max_tokens=3000):
        chunks = []
        current_chunk = []
        token_count = 0

        for item in items:
            item_str = f"Employee {item['Employee Name']} ({item['Employee ID']}) on {item['Date']}: {item['Anomaly Type']}"
            current_chunk.append(item_str)
            token_count += len(item_str.split())

            if token_count >= max_tokens:
                chunks.append(current_chunk)
                current_chunk = []
                token_count = 0

        if current_chunk:
            chunks.append(current_chunk)

        return chunks
