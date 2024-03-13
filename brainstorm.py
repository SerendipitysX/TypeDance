import openai
import os
openai.api_key = "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"

def get_answer(user_prompt):
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": user_prompt},
    {"role": "system", "content": "You are a mature logo designer. Your mission is to come up with concepts that are appropriate for symbol according to user's description. For example, given 'what can represent Chongqing', you can say the 'hot-pot' because it is the famous food in Chongqing, and you also can say 'Jie fang bei', since it is the famous landmark. Please give me five symbolize concepts and explaination, follow the format, 'xx:xx'. One concept is limited whithin one word. Using one short sententce for explanation is enough, please don't say other redundunt sentence"},
    ]
    )
    return completion.choices[0].message

def get_dict_from_answer(string):
    concepts_and_explanations = string.split("\n")[:5]

    concept_dict = {}

    for concept in concepts_and_explanations:
        parts = concept.split(": ")
        concept_name = parts[0].split(". ")[1]
        explanation = parts[1]
        
        concept_dict[concept_name] = explanation

    return concept_dict

# user_prompt = "Give some ideas about representing Chengdu"
# answer = get_answer(user_prompt)
# print(answer)
# string = answer["content"]
# concept_dict = get_dict_from_answer(string)
# print(concept_dict)