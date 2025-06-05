from crewai import Agent, Task, Crew
from agents.data_loader_agent import DataLoaderAgent
from agents.anomaly_agent import AnomalyAgent
from agents.query_agent import QueryAgent
from tools.reporting import save_anomaly_reports

class SupervisorAgent:
    def create_crew(self, excel_path):
        loader = DataLoaderAgent()
        analyzer = AnomalyAgent()
        responder = QueryAgent()

        print("[Supervisor] Step 1: Loading data...")
        df = loader.run(excel_path)

        print("[Supervisor] Step 2: Detecting anomalies...")
        anomalies = analyzer.run(df)

        print("[Supervisor] Step 3: Saving anomaly reports...")
        save_anomaly_reports(anomalies)

        print("[Supervisor] Step 4: Querying LLM with results...")
        summary = responder.run(anomalies)

        agent = Agent(
            name="SummaryAgent",
            role="Communicator",
            goal="Explain anomalies",
            backstory="Skilled in summarizing HR reports.",
            verbose=True
        )
        task = Task(description="Return final summary of anomalies.", expected_output=summary, agent=agent)
        return Crew(agents=[agent], tasks=[task])
