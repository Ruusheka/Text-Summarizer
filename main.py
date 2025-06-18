import torch
import gradio as gr


from transformers import pipeline

# model_path="Models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"
text_summary = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6",torch_dtype=torch.bfloat16)
# text_summary = pipeline("summarization", model=model_path,torch_dtype=torch.bfloat16)

# text="A mango is an edible stone fruit produced by the tropical tree Mangifera indica. It originated from the region between northwestern Myanmar, Bangladesh, and northeastern India.[1][2] M. indica has been cultivated in South and Southeast Asia since ancient times resulting in two types of modern mango cultivars: the Indian type and the Southeast Asian type.[1][2] Other species in the genus Mangifera also produce edible fruits that are also called mangoes, the majority of which are found in the Malesian ecoregion.[3]"
# print(text_summary(text))

def summary(input):
    output=text_summary(input)
    return output[0]['summary_text']

gr.close_all()

# demo=gr.Interface(fn=summary,inputs="text",outputs="text")
demo=gr.Interface(fn=summary,
                  inputs=[gr.Textbox(label="INPUT TEXT TO SUMMARIZE",lines=6)],
                  outputs=[gr.Textbox(label="SUMMARIZED TEXT",lines=4)],
                  title="TEXT SUMMARIZER",
                  description="Text Summarizer is an Application used to summarize the given text")

demo.launch()