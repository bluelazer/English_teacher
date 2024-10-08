import gradio as gr

input_list = [gr.Audio(sources=["microphone","upload"], type="filepath", label="Input Audio"),
              gr.Checkbox(label = "Checkbox"),
              gr.ColorPicker(label = "Colour Picker"),
              gr.DataFrame(label = "Data Frame"),
              gr.Dropdown(choices=["Option 1", "Option 2", "Option 3"],label = "Dropdown"),
              gr.File(label = "File"),
              gr.Image(label = "Image"),
              gr.Number(label = "Number"),
              gr.Radio(choices=["Option 1", "Option 2", "Option 3"],label = "Radio"),
              gr.Slider(label = "Slider",minimum=0, maximum=100, step=1),
              gr.Textbox(label = "Textbox", lines=3,max_lines=7,placeholder="Enter text here..."),
              gr.TextArea(label = "Text Area",lines=3,max_lines=7,placeholder="Enter text here..."),
              gr.Video(label = "Video",sources=["upload","webcam"]),]


output_list = [gr.Textbox(label = "Audio outputs"),
               gr.Textbox(label = "Checkbox outputs"),
               gr.Textbox(label = "Colour Picker outputs"),
               gr.Textbox(label = "Data Frame outputs"),
               gr.Textbox(label = "Dropdown outputs"),
               gr.Textbox(label = "File outputs"),
               gr.Textbox(label = "Image outputs"),
               gr.Textbox(label = "Number outputs"),
               gr.Textbox(label = "Radio outputs"),
               gr.Textbox(label = "Slider outputs"),
               gr.Textbox(label = "Textbox outputs"),
               gr.Textbox(label = "Text Area outputs"),
               gr.Textbox(label = "Video outputs")]

def input_and_output(*input_data):
    return input_data


iface = gr.Interface(fn = input_and_output, 
                     inputs = input_list, 
                     outputs = output_list, 
                     title = "Gradio Interface",
                     description = "This is a Gradio Interface for testing different input and output components",
                     live = True)


iface.launch()

