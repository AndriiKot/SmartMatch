# SmartMatch

This project is designed to find the most similar
song based on the text provided by the user.
It utilizes a transformer model from the `transformers`
library for vectorizing song lyrics and computes
similarity using cosine similarity.

## Technologies:

<table>
  <thead>
    <tr>
      <th height=33 width=100>Python</th>
      <th height=33 width=100>Jupyter</th>
      <th height=33 width=100>Hugging Face</th>
      <th height=33 width=100>PyTorch</th>
      <th height=33 width=100>NumPy</th>
      <th height=33 width=100>scikit-learn</th>
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
        <a href=https://scikit-learn.org/>
          <img src="https://github.com/AndriiKot/SmartMatch/blob/vectors/technologies/icons/scikit-learn.svg" alt="sciKit-learn">
        </a>
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

## Installation

To install the necessary libraries, run the following command in your Jupyter Notebook:

```python
!pip install transformers torch scikit-learn
```

## Usage

1. **Data Preparation:**
   - Create a folder named `data` in the directory where your Jupyter Notebook is located.
   - Place text files containing the song lyrics in this folder. Make sure all files have a `.txt` extension.

2. **Running the Program:**
   - Open your Jupyter Notebook.
   - Copy and paste the provided program code into the cells of your notebook.
   - Execute the cells in the following order:
     - A cell for importing libraries and loading the song lyrics.
     - A cell for inputting the user text and searching for a similar song.

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
