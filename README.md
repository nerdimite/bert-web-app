# React Web App with Flask Backend for PyTorch Model

### FullStack AI Series- Part 2 (CellStrat AI Lab)

This repository contains the code for React Web App with Flask Backend for PyTorch Model Session and is a part of the Full stack AI Love Coding Series at CellStrat AI Lab.

In this part, the BERT model that was trained in part 1 is wrapped around a React Frontend and Flask Backend for inference.

Checkout the code from the other parts here:

- [Part 1](https://github.com/theneuralbeing/bert-finetuning-webinar)
- [Part 3](https://github.com/theneuralbeing/bert-deployment-aws)

#### Usage

1. Clone the repository

```bash
git clone https://github.com/theneuralbeing/bert-web-app.git
```
2. Install the required python libraries by running `pip install -r requirements.txt`.
3. Install `node.js` for running the react application.

4. Download the trained sentiment analysis model [inference.pth](https://gradient-fire.s3.amazonaws.com/bert-webinar/inference.pth) file.
5. Move the downloaded `pth` file to the [backend](backend) directory.
6. Setup your react app by running `npm install` from the [bert-app](bert-app) directory.
7. Start your react app with `npm start` in the terminal.
8. Open another terminal and `cd` to [backend](backend) directory and start the flask server using this command `python app.py`.
9. Now you can play around with your sentiment analysis web app.
