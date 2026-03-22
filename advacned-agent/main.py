from dotenv import load_dotenv
from src.workflow import Workflow

# Load environment variables from .env file
load_dotenv()

def main():
    """
    Main function to run the advanced developer tools analysis agent.
    Initializes the workflow and handles user queries for developer tool recommendations.
    """
    # Initialize the workflow for developer tools analysis
    workflow = Workflow()
    print("Developer Tools Analysis Agent")
    
    # Main interaction loop
    while True:
        query = input("\n Developer Tools Query: ").strip()
        if query.lower() in {"quit", "exit"}:
            print("Exiting...")
            break
        if query:
            # Run the workflow with the user's query
            result = workflow.run(query)
            print(f"\nAnalysis Result for {query}:")
            print('='*60)
            # Display results for each analyzed company
            for i, company in enumerate(result.companies, 1):
                print(f"\n{i}. 🏢 {company.name}")
                print(f"   🌐 Website: {company.website}")
                print(f"   💰 Pricing: {company.pricing_model}")
                print(f"   📖 Open Source: {company.is_open_source}")

                if company.tech_stack:
                    print(f"   🛠️  Tech Stack: {', '.join(company.tech_stack[:5])}")

                if company.language_support:
                    print(
                        f"   💻 Language Support: {', '.join(company.language_support[:5])}"
                    )

                if company.api_available is not None:
                    api_status = (
                        "✅ Available" if company.api_available else "❌ Not Available"
                    )
                    print(f"   🔌 API: {api_status}")

                if company.integration_capabilities:
                    print(
                        f"   🔗 Integrations: {', '.join(company.integration_capabilities[:4])}"
                    )

                if company.description and company.description != "Analysis failed":
                    print(f"   📝 Description: {company.description}")

                print()

            # Display the final analysis/recommendations
            if result.analysis:
                print("Developer Recommendations: ")
                print("-" * 40)
                print(result.analysis)

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
