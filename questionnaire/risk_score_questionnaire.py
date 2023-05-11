
import questionary

# Maps the summed value of the responses to one of the five investor risk profiles (CHANGE to THREE)
risk_defined = {
    45: "Aggressive",
    25: "Moderate",
    5: "Conservative",
    }

# Define the questions and list of answers with corresponding numbers
questions = [
    {
        "type": "select",
        "name": "investment_objective",
        "message": "What is your investment objective and time horizon?",
        "choices": [
            {"name": "Preservation of capital (Short-term)", "value": 1},
            {"name":"Capital appreciation (Long-term)", "value": 2},
            {"name":"Income generation (Medium to Long-term)", "value": 3},
            {"name":"Speculation (Short-term)", "value": 4},
            {"name":"Growth (Long-term)", "value": 5}
        ]
    },
    {
        "type": "select",
        "name": "investment_knowledge",
        "message": "What is your investment knowledge and experience?",
        "choices": [
            {"name":"Beginner (Limited or no experience)", "value": 1},
            {"name":"Novice (Some experience, but still learning)", "value": 2},
            {"name":"Intermediate (Moderate experience and knowledge)", "value": 3},
            {"name":"Advanced (Extensive knowledge and experience)", "value": 4},
            {"name":"Expert (Professional experience and qualifications)", "value": 5}
        ]
    },
    {
        "type": "select",
        "name": "risk_tolerance",
        "message": "What is your risk tolerance level?",
        "choices": [
            {"name":"Conservative (Low risk)", "value": 1},
            {"name":"Moderately conservative (Lower to medium risk)", "value": 2},
            {"name":"Moderate (Medium risk)", "value": 3},
            {"name":"Moderately aggressive (Medium to higher risk)", "value": 4},
            {"name":"Aggressive (Higher risk)", "value": 5}
        ]
    },
    {
        "type": "select",
        "name": "investment_style",
        "message": "What is your investment style?",
        "choices": [
            {"name":"Value investing (Buying undervalued assets)", "value": 1},
            {"name":"Growth investing (Investing in high-growth companies)", "value": 2},
            {"name":"Income investing (Investing for steady income streams)", "value": 3},
            {"name":"Contrarian investing (Going against the crowd)", "value": 4},
            {"name":"Momentum investing (Investing based on market trends)", "value": 5}
        ]
    },
    {
        "type": "select",
        "name": "asset_allocation",
        "message": "What is your asset allocation preference?",
        "choices": [
            {"name":"Equities (Stocks and shares)", "value": 1},
            {"name":"Fixed income (Bonds and other fixed income securities)", "value": 2},
            {"name":"Alternatives (Hedge funds, commodities, private equity)", "value": 3},
            {"name":"Cash (Short-term investments like money market funds)", "value": 4},
            {"name":"Real estate (Property investments)", "value": 5}
        ]
    },
    {
        "type": "select",
        "name": "liquidity_requirement",
        "message": "How much liquidity do you require?",
        "choices": [
            {"name":"Low liquidity (No need for frequent access to funds)", "value": 1},
            {"name":"Moderate liquidity (Occasional need for access to funds)", "value": 2},
            {"name":"High liquidity (Frequent need for access to funds)", "value": 3},
            {"name":"Very high liquidity (Immediate access to funds required)", "value": 4},
            {"name":"Not sure/Other", "value": 5}
        ]
    },
    {
        "type": "select",
        "name": "investment_track_record",
        "message": "What is your investment track record?",
        "choices": [
            {"name":"Inexperienced (No track record)", "value": 1},
            {"name":"Poor (Negative returns or significant losses)", "value": 2},
            {"name":"Average (Average market returns or modest gains)", "value": 3},
            {"name":"Good (Above-average returns or significant gains)", "value": 4},
            {"name":"Excellent (Consistent above-average returns over time)", "value": 5}
        ]
    },
    {
        "type": "select",
        "name": "investment_attitude",
        "message": "What is your attitude towards investing?",
        "choices": [
            {"name":"Risk averse (Prefer safe and stable investments)", "value": 1},
            {"name":"Cautiously optimistic (Prefer some risk for potential gains)", "value": 2},
            {"name":"Confident (Comfortable taking calculated risks)", "value": 3},
            {"name":"Adventurous (Willing to take significant risks)", "value": 4},
            {"name":"Not sure/Other", "value": 5}
        ]
    },
    {
        "type": "select",
        "name": "diversification_level",
        "message": "What is your level of diversification preference?",
        "choices": [
            {"name":"Concentrated (Fewer investments, higher risk)", "value": 1},
            {"name":"Moderately diversified (Some diversification, some risk)", "value": 2},
            {"name":"Well-diversified (High level of diversification, lower risk)", "value":  3},
            {"name":"Very well-diversified (Extensive diversification, very low risk)", "value": 4},
            {"name":"Not sure/Other", "value": 5}
        ]
    },
    {
        "type": "select",
        "name": "expected_return",
        "message": "What is your investment return expectation?",
        "choices": [
            {"name":"Very low (Below market returns)", "value": 1},
            {"name":"Low (Market returns or slightly below)", "value": 2},
            {"name":"Average (Market returns)", "value": 3},
            {"name":"High (Above market returns)", "value": 4},
            {"name":"Very high (Significantly above market returns)", "value": 5}
        ]
    },
]

# Use questionary to prompt the user for their answers
def risk_questions():
    answers = questionary.prompt(questions)
    # Sum the values of the user's responses
    risk_score = 0
    for answer in answers.values():
        if isinstance(answer, int):
            risk_score += answer
        else:
            risk_score += answer.get("value")
    print(f"Your risk score is: {risk_score}")
    return True

def risk_mapping():
    risk_score = 10
    for key, risk_profile in risk_defined.items():
    # for risk_profile in risk_defined.items():
    #     return risk_profile
        if risk_score >= key:
            print(f'Your risk profile is {risk_profile}')
            return risk_profile

# print((f"Your risk score is: {risk_score}"))
   

# Print the total score
# print(f"Your risk score is: {risk_score}")

# Returns the Investor Risk Profile


##################### FUTURE FEATURE ##############################
############ AS OF 20230511, USING SET AMOUNT OF $100K ############
# Ask user how much money they want to invest
# Verify the amount is an integer

# def is_number(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False

# investment_amount = questionary.text(
#     "How much do you want to invest?",
#     validate=is_number
# ).ask()

# print("You would like to invest: $", investment_amount)
#####################################################################