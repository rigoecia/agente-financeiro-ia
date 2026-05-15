from services.llm_service import generate_response
from services.analytics_service import analyze_transactions
from agent.guardrails import validate_response

class FinancialAgent:

    def ask(self, question):

        context = analyze_transactions()

        response = generate_response(question, context)

        safe_response = validate_response(response)

        return safe_response