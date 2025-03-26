import os
from gemini import generate_text
from uipath import analyze_xaml_file

def convert_to_powerautomate(file_path):
    """
    Converts UiPath workflow analysis to a Power Automate Copilot task description.
    
    Args:
        file_path (str): Path to the UiPath XAML file.
    
    Returns:
        str: Copilot-compatible Power Automate workflow description.
    """
    try:
        # Analyze the XAML file using the function from uipath.py
        uipath_analysis = analyze_xaml_file(file_path)

        prompt = f"""
        Objective: Automate UiPath to Power Automate Workflow Conversion for Copilot

        Context: You are an expert automation architect fluent in UiPath and Power Automate. Convert a detailed UiPath workflow analysis into a Power Automate flow optimized for Copilot. Use in-depth knowledge of activity mapping, data type conversions, and cloud automation best practices. Prioritize accuracy and completeness. Refer to provided documentation for both platforms.

        Documentation Resources (CRITICAL):
        * UiPath: [https://docs.uipath.com/](https://docs.uipath.com/) - Understand the UiPath activity function.
        * Power Automate: [https://learn.microsoft.com/en-us/power-automate/](https://learn.microsoft.com/en-us/power-automate/) - Identify the equivalent Power Automate action and its limitations.

        Input: UiPath Workflow Analysis:

        {uipath_analysis}

        Detailed Output Requirements (Maximum 400 words):

        Workflow Summary (Copilot-Friendly): Provide a concise, natural language description of the Power Automate workflow's purpose for Copilot. Focus on the outcome (1-2 sentences).

        Component Sequence (Power Automate Actions): List Power Automate components present in the documentation only and must create flow (actions, triggers, connectors) in execution order. No special characters, no examples. Use natural language. For each component:

        Power Automate Action Name: The official Power Automate action name.

        Emphasis:

        Accuracy: Correct mapping of UiPath activities to Power Automate actions is critical.
        Completeness: Account for all activities and logic in the UiPath workflow analysis.
        Clarity: Easy-to-understand and implement in Power Automate.
        Copilot Readiness: Workflow summary should be easily understood by Copilot.
        """
        
        try:
            response = generate_text(prompt)
            if not response:
                raise ValueError("Error: Empty response received from Gemini.")
            return response
        except Exception as e:
            raise RuntimeError(f"Gemini API Error: {e}")
    
    except Exception as e:
        return f"Unexpected Error: {e}"

# Example usage
if __name__ == "__main__":
    file_path = input("Enter the path to your XAML file: ")
    output = convert_to_powerautomate(file_path)
    print("\nGenerated Power Automate Copilot Task:\n")
    print(output)

