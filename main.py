# main.py
from crewai import Crew
from agents.supervisor_agent import SupervisorAgent
from config import EXCEL_PATH

if __name__ == "__main__":
    print("\n=== CrewAI Timesheet Supervisor ===\n")
    supervisor = SupervisorAgent()
    crew: Crew = supervisor.create_crew(EXCEL_PATH)
    result = crew.kickoff()
    print("\n=== Summary ===\n")
    print(result)
