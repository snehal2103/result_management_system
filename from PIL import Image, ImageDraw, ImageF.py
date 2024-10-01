from PIL import Image, ImageDraw, ImageFont

def generate_certificate(student_name, course_name, certificate_template, font_path, output_path):
    # Opens the certificate template image
    img = image.open(certificate_template, mode='r')

    # Gets the image width and height
    image_width, image_height = img.size

    # Creates a drawing canvas overlay on top of the image
    draw = ImageDraw.Draw(img)

    # Gets the font object from the font file (TTF)
    font_size = 100  # Change this according to your needs
    font = ImageFont.truetype(font_path, font_size)

    # Fetches the text width for calculations later on
    text_width, _ = draw.textlength(student_name, font=font)

    # Calculates the position to center the student name on the certificate
    text_x_position = (image_width - text_width) / 2
    text_y_position = 600  # Adjust this according to your needs

    # Draws student name on the certificate
    draw.text((text_x_position, text_y_position), student_name, fill="black", font=font)

    # Fetches the text width for the course name
    text_width, _ = draw.textlength(course_name, font=font)

    # Calculates the position to center the course name on the certificate
    text_x_position = (image_width - text_width) / 2
    text_y_position += font_size + 20  # Adds some spacing between student name and course name

    # Draws course name on the certificate
    draw.text((text_x_position, text_y_position), course_name, fill="black", font=font)

    # Saves the image in PNG format
    img.save(output_path)

# Driver code
if __name__ == "__main__":
    student_name = "John Doe"  # Replace this with the actual student name
    course_name = "Computer Science"  # Replace this with the actual course name
    certificate_template = "P(1).jpeg"
    font_path = "LCALLIG.TTF"  # Path to the font file (TTF)
    output_path = "RMS/certificate.png"  # Output path for the generated certificate

    generate_certificate(student_name, course_name, certificate_template, font_path, output_path)
