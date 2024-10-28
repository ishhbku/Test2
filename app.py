import gradio as gr

def add_numbers(a, b):
    return a + b

# Set up Gradio interface
interface = gr.Interface(fn=add_numbers, 
                         inputs=[gr.Number(label="Input A"), gr.Number(label="Input B")], 
                         outputs="number",
                         title="Simple Addition App",
                         description="Enter two numbers to get their sum.")

# Launch Gradio interface
interface.launch()
