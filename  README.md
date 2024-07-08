# Image Similarity Search Application

![Streamlit App](./assets/app_screenshot.png)

This project is a Streamlit-based application for performing image similarity search using embeddings stored in Qdrant.

## Features

- Fetches initial records from a Qdrant collection and displays images.
- Allows users to select a record and find similar images based on embeddings.
- Supports caching of QdrantClient instance for efficiency.
- Converts base64-encoded image strings to bytes for rendering images in Streamlit.
- Dynamically resizes and preprocesses images using PIL and converts them to base64 format.
- Utilizes Transformers and PyTorch for image embedding generation.
- I used "microsoft/resnet-50" for the image embedding.
- Integrates dotenv for managing environment variables securely.

## Setup

To run this project locally, follow these steps:

### Prerequisites

- Python 3.9 or higher
- Pip package manager
- Qdrant setup with collection created

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/surbhi498/ImageSearchEngine.git
   cd streamlit
   
### Run the command**   
```bash
streamlit run app.py


### Visit Our Deplyed Application

You can visit our website [here](https://bby4nz8tfecnwbffyy7wnn.streamlit.app/).