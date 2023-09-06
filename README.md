# Content Based Image Retrieval

The Content Based Image Retrieval project is a Python application that focuses on image recognition and retrieval based on content characteristics. It uses various techniques, including color projection and barcode comparison, to enhance the accuracy of image retrieval.

## Project Overview

The Content Based Image Retrieval project addresses the challenge of retrieving images from a database based on their content. By leveraging advanced image analysis techniques, this application provides a way to search for images with similar visual features, allowing users to quickly find relevant images.

## Getting Started

### Prerequisites

To run this project, you'll need Python installed on your machine. Additionally, you'll need the following libraries:
- Pillow: Image processing library
- Pygame: Library for creating interactive games and simulations

You can install these libraries using the following commands:

```
pip install pillow
pip install pygame
```

### Running the Retrieval Application

1. Clone the repository to your local machine.

2. Navigate to the project directory in your terminal.

3. Run the retrieval application:

```
python main.py
```

## Features and Usage

The Content Based Image Retrieval application allows users to:
- Input an image for which similar images are to be retrieved.
- Utilize color projection and barcode comparison for enhanced retrieval.
- View a list of retrieved images with similar visual characteristics.

## Technologies Used

This project is developed using:
- Python: Core programming language.
- Pillow: Library for image processing and manipulation.
- Pygame: Library for interactive graphical applications.

## How It Works

1. The application analyzes the input image's color distribution and retrieves its grayscale values.
2. It calculates four different projections of the image: horizontal, vertical, 45 degrees, and 135 degrees.
3. The projections are transformed into a barcode, representing the image's visual characteristics.
4. The user's input image is compared with the database using the calculated barcode.
5. The retrieved image with the closest barcode is displayed to the user.

## Screenshots

![CBIR 0](https://user-images.githubusercontent.com/93552245/196062983-2c24cbc7-d504-4bfe-b901-2158fd2df3fb.PNG)
![CBIR 3](https://user-images.githubusercontent.com/93552245/196062987-d8d4aa25-62fd-4172-be3c-83b611818623.PNG)
![CBIR 5](https://user-images.githubusercontent.com/93552245/196062990-e356326b-ff74-416a-bc7a-ed2087dcb2e5.PNG)
![CBIR 8](https://user-images.githubusercontent.com/93552245/196062991-80d334b5-00c9-407d-ace2-2f02875b67cc.PNG)

## Future Enhancements

- Implement more advanced image recognition techniques.
- Allow users to upload images from their devices.
- Provide options for refining retrieval results based on different features.

## Portfolio

For more projects and information about me, check out my [Portfolio](https://abdulshahid.net/).

## Contact

If you have any questions or would like to discuss this project further, feel free to contact me on [LinkedIn](https://www.linkedin.com/in/abdul-shahid-otu/).
