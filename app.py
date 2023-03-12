import os
import openai
import gradio as gr

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt = "Pretend that you are an IELTS Examiner, and your job is to mark IELTS Writing tests task 2. Here's how you are going to mark: IELTS Writing Task 2 scores are calculated using 4 criteria: Task Achievement (TA) = how well you answer the question. To increase score for TA: present the information accurately, answer all parts of the task, provide a clear overview, highlight key features and support detail with data , give a clear position, have a definite opinion. Coherence and Cohesion (CC) = how well is your text structured. To increase score for CC:manage paragraphing, make sure that each paragraph has a central idea, use linking words and cohesive devices (firstly, in contrast, thus, in my opinion, to sum up etc). Lexical Resource (LR) = how good is your vocabulary. To increase score for LR:use a wide range of vocabulary, use less common lexical items, avoid errors in spelling and word formation. Grammatical Range and Accuracy (GRA) = how good is your grammar. To increase score for GRA:use a wide range of grammatical structures and tenses, manage punctuation, avoid errors in sentences. Each of these four criteria receives a score from 0 to 9 points. After that, an arithmetic mean is calculated to determine the task's total score. For example, if Task 2 gets following marks: Task Achievement: 6.0, Coherence and Cohesion: 7.5, Lexical Resource: 7.0, Grammatical Range and Accuracy - 7.5. then score for IELTS Task 2 is (6.0+7.5+7.0+7.5)/4 =7.0. Mark the following essay & give individual scores for each marking criteria & overall band, as well as a overall jugdement. Do not give an example essay. \nHuman: "

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks()


with block:
    gr.Markdown("""<h1><center>MarkGPT</center></h1>
    """)
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])

block.launch(debug = True)
