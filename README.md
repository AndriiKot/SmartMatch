# SmartMatch
### Please note that Python version 3.13 may not work correctly with the 'PyTorch' library!

This project is designed to find the most similar song based on the text provided by the user. It utilizes a transformer model from the `transformers` library for vectorizing song lyrics and computes similarity using cosine similarity.

## Technologies:

<table>
  <thead>
    <tr>
      <th height=33 width=100>Python</th>
      <th height=33 width=100>Jupyter</th>
      <th height=33 width=100>Hugging Face</th>
      <th height=33 width=100>PyTorch</th>
      <th height=33 width=100>NumPy</th>
      <th height=33 width=100>Faiss</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td height=100 width=100>
        <a href=https://www.python.org/>
          <img src=https://github.com/AndriiKot/SmartMatch/blob/main/technologies/icons/python.svg alt=Python>
        </a>
      </td>
      <td height=100 width=100>
        <a href=https://jupyter.org/>
          <img src=https://github.com/AndriiKot/SmartMatch/blob/main/technologies/icons/jupyter.svg alt=Jupyter>
        </a>
      </td>
      <td height=100 width=100>
        <a href=https://huggingface.co/>
          <img src=https://github.com/AndriiKot/SmartMatch/blob/vectors/technologies/icons/huggingface.svg alt="Hugging Face">
        </a>
      </td>
      <td height=100 width=100>
        <a href=https://pytorch.org/>
          <img src=https://github.com/AndriiKot/SmartMatch/blob/vectors/technologies/icons/pytorch.svg alt="PyTorch">
        </a>
      </td>
      <td height=100 width=100>
        <a href=https://numpy.org/>
          <img src=https://github.com/AndriiKot/SmartMatch/blob/vectors/technologies/icons/numpy.svg alt="NumPy">
        </a>
      </td>
      <td height=100 width=100>
        <h2>Faiss</h2>
      </td>
    </tr>
  </tbody>
</table>

## Contents

- [Functionality](#functionality)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)

## Functionality

The program allows you to:
- Load song lyrics from text files.
- Vectorize song lyrics using the `distilbert-base-uncased` model.
- Find the most similar song based on the user-provided text.

## Requirements

To run the program, you need to install the following libraries:
- `transformers`
- `torch`
- `scikit-learn`

> **Note:** If you are running the code outside of a Jupyter Notebook, it is recommended to use Python version 3.10 or higher.

## Installation

To install the necessary libraries, run the following command in your terminal:

```bash
pip install transformers torch scikit-learn
```

## Usage

1. **Data Preparation:**
   - Create a folder named `data` in the directory where your script is located.
   - Place text files containing the song lyrics in this folder. Make sure all files have a `.txt` extension.

2. **Running the Program:**
   - If you are using Jupyter Notebook, open your notebook and proceed as described below.
   - If you are not using Jupyter, save the following initial code to a file named `main.py` and run it using the command:

   ```bash
   py -3.10 main.py
   ```
or

   ```bash
   py -3.11 main.py
   ```
## Attention


   - Copy and paste the provided program code into your script.

3. **Text Input:**
   - After running the code, enter the text for which you want to find a similar song when prompted.

   Example code for text input:
   ```python
   user_input = input("Please enter the text you want to find a similar song for: ")
   similar_song_name, similarity_score = find_similar_song(user_input)
   print(f"The most similar song is: {similar_song_name} with a similarity score of {similarity_score:.4f}")
   ```

## Notes

- If you do not have a Graphics Processing Unit (GPU), make sure that `PyTorch` is installed with CPU support, or simply use the CPU as your device.
- Depending on the volume of songs you have loaded and the power of your computer, vector calculation may take some time.

## License

This project is licensed under the MIT License. Please refer to the LICENSE file for more details.
