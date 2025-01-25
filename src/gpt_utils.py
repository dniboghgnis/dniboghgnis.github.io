# Description: This file contains the utility functions for the GPT model.
def call_gemini_api(query = "Explain how AI works in hindi"):
    import google.generativeai as genai
    api_key = "AIzaSyAOziZimq507ZLgnmsjaFg1YYpk0pgz5Uc"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(query)
    print(response.text)
    return response.text
