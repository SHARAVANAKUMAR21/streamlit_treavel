import streamlit as st
import google.generativeai as genai

# Set up the Google Generative AI API key
api_key = 'AIzaSyAVfwfMaAKqxThTKMaBqGSHCSbdyUOMxAE'
genai.configure(api_key=api_key)

# Define the 10 MCQs
questions = [
    {"question": "What type of climate do you prefer?", "options": ["Warm", "Cold", "Tropical", "Mild"]},
    {"question": "What kind of activities do you enjoy?", "options": ["Adventure", "Relaxation", "Cultural", "Nature"]},
    {"question": "Do you prefer city or countryside?", "options": ["City", "Countryside"]},
    {"question": "What is your ideal accommodation?", "options": ["Hotel", "Resort", "Hostel", "Vacation rental"]},
    {"question": "What type of cuisine do you prefer?", "options": ["Local", "International", "Vegetarian", "Vegan"]},
    {"question": "What type of transportation do you prefer?", "options": ["Public transport", "Car rental", "Walking"]},
    {"question": "Do you prefer traveling alone or in a group?", "options": ["Alone", "Group"]},
    {"question": "What is your travel budget?", "options": ["Low", "Moderate", "High"]},
    {"question": "What kind of attractions do you like?", "options": ["Historical", "Natural", "Amusement parks", "Beaches"]},
    {"question": "Do you prefer a fast-paced or relaxed vacation?", "options": ["Fast-paced", "Relaxed"]}
]

def main():
    st.title("Travel Destination Recommender")
    st.write("Answer the following questions to find the best travel destination for you!")

    # Collect answers for the 10 MCQs
    user_answers = {}
    for i, q in enumerate(questions):
        user_answers[q["question"]] = st.radio(q["question"], q["options"])

    # Button to submit answers and generate recommendation
    if st.button("Generate Recommendation"):
        # Formulate the prompt based on user's answers
        prompt = "Based on the following preferences, recommend the best travel destination:\n"
        for question, answer in user_answers.items():
            prompt += f"{question}: {answer}\n"

        try:
            # Use the Generative AI model to generate a travel recommendation
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            travel_recommendation = response.text

            # Display the recommendation
            st.subheader("Your Recommended Travel Destination:")
            st.write(travel_recommendation)

        except Exception as e:
            st.error(f"An error occurred: {e}")
            st.warning("We couldn't generate the recommendation. Please try again later.")

if __name__ == "__main__":
    main()
