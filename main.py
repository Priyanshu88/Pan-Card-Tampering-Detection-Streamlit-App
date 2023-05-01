import cv2
import numpy as np
import streamlit as st
from skimage.metrics import structural_similarity as ssim


def process_image(image, reference):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize the image to a fixed size
    size = (600, 400)
    resized = cv2.resize(gray, size, interpolation=cv2.INTER_AREA)

    # Compute the structural similarity index
    ssim_index = ssim(resized, reference)

    # Apply thresholding to detect tampering
    threshold = 0.8
    tampering_detected = ssim_index < threshold

    # Find contours in the image
    contours, hierarchy = cv2.findContours(resized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return tampering_detected, ssim_index, contours


def draw_contours(image, contours):
    # Draw the contours on the image
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > 100:
            cv2.drawContours(image, contours, i, (0, 0, 255), 2)


# Define the Streamlit app
def main():
    st.set_page_config(page_title='PAN Card Tampering Detection')

    # Add a title and subtitle
    st.title('PAN Card Tampering Detection')
    st.write('Upload an image of a PAN card to detect tampering and validate the ID.')

    # Load the reference image
    reference_image = cv2.imread('reference.jpg', cv2.IMREAD_GRAYSCALE)
    reference_image_resized = cv2.resize(reference_image, (600, 400), interpolation=cv2.INTER_AREA)

    # Add a file uploader to get the image from the user
    uploaded_file = st.file_uploader('Choose an image file', type=['jpg', 'jpeg', 'png'])

    # Process the uploaded image and display the results
    if uploaded_file is not None:
        # Read the image
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)

        # Process the image
        tampering_detected, ssim_index, contours = process_image(image, reference_image_resized)

        # Draw the contours on the image
        draw_contours(image, contours)

        # Display the image and results
        st.image(image, channels='BGR', use_column_width=True)
        if tampering_detected:
            st.error('Tampering detected!')
        else:
            st.success('No tampering detected.')
        st.write(f'Structural similarity index: {ssim_index:.2f}')


if __name__ == '__main__':
    main()

