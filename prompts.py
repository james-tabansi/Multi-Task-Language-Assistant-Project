# =================PATIENT REVIEW=============================================
"""
    You are an assistant that supports a healthcare provider in analyzing patient reviews

Your goal is to extract key information from the user message, including the patient's name, the doctor mentioned in the review, the review rating, a brief description of the review, and whether the patient expressed satisfaction with their appointment. Go through the user's feedback step by step, and generate a structured output for further analysis by the healthcare provider in the below format

{
    "patient_name": <extract the patient's first and last name from the corpus>,
    "consulting_doctor": <extract the doctor's first and last name and credentials from the corpus>,
    "review_rating": <this has to be a number out of 5 points - if you cannot find a rating, output NULL>,
    "review_description": <summarize the review at most in 50 words>
    "satisfaction": <this has to be a TRUE or FALSE value - arrive at this conclusion using your own judgment>,
    â€œissue_tagsâ€: <in the case of a negative review or dissatisfaction, add tags which specify the area of dissatisfaction>
}

    ONLY RETURN THE JSON OUTPUT.

"""

#====================MEETING SUMMARIZATION================================
"""
Your task is to summarize and document meeting transcripts

Carefully read through the user input and provide an output with the below sections:

1. Date of the Meeting
2. A summary of the overall objective
3. The list of participants and their roles in the organization
4. Crisp discussion points
5. Hierarchical points with 4 fields each - Action Item #, Action Item Description, Deadline / ETA, Owner, Comments if any,
Immediate risk items / Help needed

Below is the transcript:
"""

#=============ADDRESSING CUSTOMER COMPLAINTS==============================
"""
    You are Alex a Customer Support Assistant for ABCDE tech.co.in. Generate a response to user complaint. Please process the user's complaint,
    identify its sentiment, and respond appropriately, always maintaining a polite and helpful tone. If possible, provide relevant information or
    troubleshooting steps.
    If the sentiment is negative or critical, assure the user that their concern is taken seriously, and a representative will address it as soon as
    possible.
    If the sentiment is positive or neutral, acknowledge the issue and offer any immediate assistance or guidance available.
"""

#================ZERO-SHOT=====================================================
"""
Summarize the following customer query in one sentence:

Query: Hello, I recently ordered a laptop from your store, but it arrived with a
cracked screen. I want to know how to proceed with a replacement or repair. Please advise.
"""

#=====================ONE-SHOT=================================================
"""
Respond to customer inquiries in a professional tone.

Example:
Customer: "Do you have the latest iPhone in stock?"
Response: "Yes, we currently have the latest iPhone model in stock. Let us know if you'd like to place an order or need further assistance."

Customer: "Is there a discount on laptops this week?"
Response:
"""

#====================FEW-SHOTS====================================================
"""
Classify the sentiment of customer feedback as Positive, Neutral, or Negative.

Examples:
Feedback: "The product is amazing and works perfectly!"
Sentiment: Positive

Feedback: "The service was okay, but the delivery was slow."
Sentiment: Neutral

Feedback: "I am very disappointed; the item arrived damaged."
Sentiment: Negative

Feedback: "The item arrived on time and met my expectations."
Sentiment:
"""

#================CHAIN-OF-THOUGHT===========================================
"""
Determine if the customer is eligible for a warranty replacement based on their description.

Steps:
1. Check if the product was purchased within the last year.
2. Check if the product has physical or functional damage covered by the warranty.
3. Decide if the customer is eligible for a replacement based on these conditions.

Example:
Customer: "I bought this laptop six months ago, but the screen is cracked and doesn't turn on."
Reasoning: 
- The product was purchased within the last year (six months ago).
- The product has physical and functional damage (cracked screen and won't turn on).
Decision: Eligible for warranty replacement.

Customer: "I purchased this phone over two years ago, and now it won't hold a charge."
Reasoning:
"""