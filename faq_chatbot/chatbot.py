import spacy

nlp = spacy.load("en_core_web_sm")

# Define some example FAQs
FAQ_PAIRS = {
    "Hi":"Hello! How Can I help You Today",
    "What is your name?": "I am a chatbot created to answer FAQs.",
    "How do I use this product?": "To use this product, follow the instructions in the user manual.",
    "What is the return policy?": "You can return the product within 30 days for a full refund.",
    "What are the shipping options?": "We offer standard and express shipping options.",
    "What is your return policy?": "Our return policy allows returns within 30 days of purchase with a valid receipt.",
    "How can I track my order?": "You can track your order by logging into your account and visiting the 'Order History' section.",
    "Do you offer international shipping?": "Yes, we offer international shipping. Please check our shipping policy for more details.",
    "What payment methods do you accept?": "We accept credit/debit cards, PayPal, and bank transfers.",
    "How can I reset my password?": "To reset your password, go to the login page and click on 'Forgot Password'.",
    "What are your customer support hours?": "Our customer support is available 24/7.",
    "How do I contact customer support?": "You can contact customer support via email at support@example.com or call us at +123-456-7890.",
    "Can I change my shipping address after placing an order?": "You can change your shipping address within 24 hours of placing the order by contacting customer support.",
    "Do you have a mobile app?": "Yes, we have a mobile app available on both iOS and Android platforms. Search for 'Our App' in the app stores.",
    "How can I apply a discount code?": "You can apply a discount code at checkout by entering it in the 'Discount Code' field.",
    "What is your privacy policy?": "Our privacy policy can be viewed on our website under the 'Privacy Policy' section.",
    "Can I cancel my order?": "Yes, you can cancel your order within 24 hours of placing it by contacting customer support.",
    "What is your warranty policy?": "We offer a one-year warranty for all our products. Please check our warranty policy for more details.",
    "How do I subscribe to your newsletter?": "You can subscribe to our newsletter by entering your email address in the subscription box on our homepage.",
    "What is the estimated delivery time?": "The estimated delivery time is 3-7 business days, depending on your location.",
    "How do I create an account?": "To create an account, click on the 'Sign Up' button on our website and fill in the required details.",
    "Are there any membership benefits?": "Yes, members get exclusive discounts, early access to sales, and more.",
    "What should I do if I receive a damaged product?": "If you receive a damaged product, please contact our customer support immediately for a replacement or refund.",
    "Do you provide gift wrapping services?": "Yes, we offer gift wrapping services at an additional cost.",
    "How do I leave a review for a product?": "To leave a review, go to the product page and click on 'Write a Review'.",
    "What is your exchange policy?": "We offer exchanges within 30 days of purchase. Please check our exchange policy for more details.",
    "How do I redeem my loyalty points?": "You can redeem your loyalty points at checkout by selecting the 'Use Loyalty Points' option.",
    "Is there a minimum order value for free shipping?": "Yes, orders above $50 are eligible for free shipping.",
    "Can I save items to a wishlist?": "Yes, you can save items to your wishlist by clicking the 'Add to Wishlist' button on the product page.",
    "Do you offer student discounts?": "Yes, we offer a 10% discount for students. Please verify your student status to avail the discount.",
}

def get_response(user_input):
    # Process user input
    user_input = nlp(user_input.lower())
    # Initialize variables
    best_match = None
    best_score = 0.0

    # Find the most similar FAQ
    for question, answer in FAQ_PAIRS.items():
        question_doc = nlp(question.lower())
        similarity = user_input.similarity(question_doc)

        if similarity > best_score:
            best_score = similarity
            best_match = answer

    # Return the best match
    if best_score > 0.6:  # You can adjust this threshold
        return best_match
    else:
        return "I'm sorry, I don't understand the question. Can you please rephrase?"

