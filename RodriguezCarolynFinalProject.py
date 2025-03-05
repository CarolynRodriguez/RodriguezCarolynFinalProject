"""
Program: Module 08 Final Project
Author" Carolyn Rodriguez
Date: 03/04/25
Purpose: A program which displays an adoption page where users can browse and enter their contact details to place adoption holds on individual pets of their choosing. 
"""

import tkinter as tk # Imports Tkinter
from tkinter import messagebox # Imports messagebox for pop up messages
from PIL import Image, ImageTk  # Imports PIL for displaying images

# Dictionary stores details for each pet
pet_details = {
    1: {
        "name": "Milo",
        "breed": "German Shepherd",
        "personality": "Friendly and energetic",
        "img_file": "pet1.jpg"  # Image file for Milo (pet 1)
    },
    2: {
        "name": "Cooper",
        "breed": "Alaskan Malamute",
        "personality": "Curious and playful",
        "img_file": "pet2.jpg" # Image file for Cooper (pet 2)
    },
    3: {
        "name": "Bella",
        "breed": "Ginger Tabby",
        "personality": "Shy and affectionate",
        "img_file": "pet3.jpg" # Image file for Bella (pet 3)
    },
    4: {
        "name": "Coco",
        "breed": "Potcake Mix",
        "personality": "Active and loud",
        "img_file": "pet4.jpg" # Image file for Coco (pet 4)
    },
    5: {
        "name": "Charlie",
        "breed": "Brown Tabby",
        "personality": "Calm and loving",
        "img_file": "pet5.jpg" # Image file for Charlie (pet 5)
    },
    6: {
        "name": "Cleo",
        "breed": "Light Orange Tabby",
        "personality": "Loyal and protective",
        "img_file": "pet6.jpg" # Image file for Cleo (pet 6)
    }
}

# Function opens a new window to display pet details
def open_pet_details(pet_number):
    details = pet_details[pet_number] # Gets details of selected pet based on pet number
    detail_window = tk.Toplevel(main_window) # Creates a new window
    detail_window.title(f"Details for {details['name']}") # Window title is set to "Details for (insert pet name)"
    
    # Loads and resizes the pet image
    img = Image.open(details["img_file"]) # Opens pet image
    img = img.resize((300, 300)) # Sizes image to 300 x 300
    pet_photo = ImageTk.PhotoImage(img) # Uses Tkinter to display image
    
    # Keeps image to display in details window
    detail_window.pet_photo = pet_photo
    
    # Displays the pet's image in details window
    image_label = tk.Label(detail_window, image=pet_photo)
    image_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    
    # Displays pet name
    name_label = tk.Label(detail_window, text=f"Name: {details['name']}")
    name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    # Displays pet breed
    breed_label = tk.Label(detail_window, text=f"Breed: {details['breed']}")
    breed_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    # Displays pet personality
    personality_label = tk.Label(detail_window, text=f"Personality: {details['personality']}")
    personality_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    
    # Buttons for details window
    tk.Button(detail_window, text="Adopt", command=lambda: open_adoption_form(details['name'])).grid(row=4, column=0, padx=10, pady=10)
    # Adds button to open adoption form window
    tk.Button(detail_window, text="Back", command=detail_window.destroy).grid(row=4, column=1, padx=10, pady=10)
    # Adds button to close details window which returns user to main window

# Function to open adoption form window
def open_adoption_form(pet_name):
    adoption_window = tk.Toplevel(main_window) # Creates a new pop up window
    adoption_window.title("Adoption Hold Confirmation") # Sets window title to "Adoption Hold Confirmation"

    # Label to confirm pet adoption
    tk.Label(adoption_window, text=f"Confirm a 24-hour hold for {pet_name}").grid(row=0, column=0, columnspan=2, pady=10)

    # Asks user for contact details 
    tk.Label(adoption_window, text="Your Name:").grid(row=1, column=0, padx=10, pady=5) # User name input
    name_entry = tk.Entry(adoption_window)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(adoption_window, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5) # User phone number input
    phone_entry = tk.Entry(adoption_window)
    phone_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(adoption_window, text="Email Address:").grid(row=3, column=0, padx=10, pady=5) # User email input
    email_entry = tk.Entry(adoption_window)
    email_entry.grid(row=3, column=1, padx=10, pady=5)

    # Function to validate and confirm the adoption hold
    def confirm_adoption():
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()

        if not name or not phone or not email:
            messagebox.showerror("Error", "All fields are required!") # Error if fields are empty
            return
        
        if not phone.isdigit():
            messagebox.showerror("Error", "Phone number should contain only digits!") # Validates phone number (digits only)
            return
        if "@" not in email or "." not in email:
            messagebox.showerror("Error", "Enter a valid email address!") # Validates email format
            return
        
        # Shows confirmation message
        messagebox.showinfo("Success", f"Adoption hold confirmed for {pet_name}!\nWe will contact you soon.")
        # Closes adoption window
        adoption_window.destroy()

    # Button to confirm adoption
    tk.Button(adoption_window, text="Confirm", command=confirm_adoption).grid(row=4, column=0, pady=10, padx=5)
    # Buttons to close window, returns user to previous windows
    tk.Button(adoption_window, text="Back", command=adoption_window.destroy).grid(row=4, column=1, pady=10, padx=5)

# Main application window
main_window = tk.Tk()
main_window.title("Loving Paws Shelter Adoption Page") # Sets title name to "Loving Paws Sheler Adoption Page"

# Welcome message at the top of the main window
welcome_label = tk.Label(main_window, text="Welcome to the Loving Paws Shelter Adoption Page")
welcome_label.grid(row=0, column=0, columnspan=3, pady=10)

# Loads each pet image for the main window and resizes them to 150 x 150
pet1_img = Image.open("pet1.jpg")
pet1_img = pet1_img.resize((150, 150))
pet1_photo = ImageTk.PhotoImage(pet1_img)

pet2_img = Image.open("pet2.jpg")
pet2_img = pet2_img.resize((150, 150))
pet2_photo = ImageTk.PhotoImage(pet2_img)

pet3_img = Image.open("pet3.jpg")
pet3_img = pet3_img.resize((150, 150))
pet3_photo = ImageTk.PhotoImage(pet3_img)

pet4_img = Image.open("pet4.jpg")
pet4_img = pet4_img.resize((150, 150))
pet4_photo = ImageTk.PhotoImage(pet4_img)

pet5_img = Image.open("pet5.jpg")
pet5_img = pet5_img.resize((150, 150))
pet5_photo = ImageTk.PhotoImage(pet5_img)

pet6_img = Image.open("pet6.jpg")
pet6_img = pet6_img.resize((150, 150))
pet6_photo = ImageTk.PhotoImage(pet6_img)

# Pet Frame 1 (Row 1, Column 0)
pet_frame1 = tk.Frame(main_window, borderwidth=1, relief="solid", padx=5, pady=5)
pet_frame1.grid(row=1, column=0, padx=10, pady=10)
pet_image_label1 = tk.Label(pet_frame1, image=pet1_photo, borderwidth=1)
pet_image_label1.grid(row=0, column=0, pady=(0, 5))
pet_label1 = tk.Label(pet_frame1, text="Milo")
pet_label1.grid(row=1, column=0, pady=(0, 5))
details_button1 = tk.Button(pet_frame1, text="View Details", command=lambda: open_pet_details(1))
details_button1.grid(row=2, column=0)

# Pet Frame 2 (Row 1, Column 1)
pet_frame2 = tk.Frame(main_window, borderwidth=1, relief="solid", padx=5, pady=5)
pet_frame2.grid(row=1, column=1, padx=10, pady=10)
pet_image_label2 = tk.Label(pet_frame2, image=pet2_photo, borderwidth=1)
pet_image_label2.grid(row=0, column=0, pady=(0, 5))
pet_label2 = tk.Label(pet_frame2, text="Cooper")
pet_label2.grid(row=1, column=0, pady=(0, 5))
details_button2 = tk.Button(pet_frame2, text="View Details", command=lambda: open_pet_details(2))
details_button2.grid(row=2, column=0)

# Pet Frame 3 (Row 1, Column 2)
pet_frame3 = tk.Frame(main_window, borderwidth=1, relief="solid", padx=5, pady=5)
pet_frame3.grid(row=1, column=2, padx=10, pady=10)
pet_image_label3 = tk.Label(pet_frame3, image=pet3_photo, borderwidth=1)
pet_image_label3.grid(row=0, column=0, pady=(0, 5))
pet_label3 = tk.Label(pet_frame3, text="Bella")
pet_label3.grid(row=1, column=0, pady=(0, 5))
details_button3 = tk.Button(pet_frame3, text="View Details", command=lambda: open_pet_details(3))
details_button3.grid(row=2, column=0)

# Pet Frame 4 (Row 2, Column 0)
pet_frame4 = tk.Frame(main_window, borderwidth=1, relief="solid", padx=5, pady=5)
pet_frame4.grid(row=2, column=0, padx=10, pady=10)
pet_image_label4 = tk.Label(pet_frame4, image=pet4_photo, borderwidth=1)
pet_image_label4.grid(row=0, column=0, pady=(0, 5))
pet_label4 = tk.Label(pet_frame4, text="Coco")
pet_label4.grid(row=1, column=0, pady=(0, 5))
details_button4 = tk.Button(pet_frame4, text="View Details", command=lambda: open_pet_details(4))
details_button4.grid(row=2, column=0)

# Pet Frame 5 (Row 2, Column 1)
pet_frame5 = tk.Frame(main_window, borderwidth=1, relief="solid", padx=5, pady=5)
pet_frame5.grid(row=2, column=1, padx=10, pady=10)
pet_image_label5 = tk.Label(pet_frame5, image=pet5_photo, borderwidth=1)
pet_image_label5.grid(row=0, column=0, pady=(0, 5))
pet_label5 = tk.Label(pet_frame5, text="Charlie")
pet_label5.grid(row=1, column=0, pady=(0, 5))
details_button5 = tk.Button(pet_frame5, text="View Details", command=lambda: open_pet_details(5))
details_button5.grid(row=2, column=0)

# Pet Frame 6 (Row 2, Column 2)
pet_frame6 = tk.Frame(main_window, borderwidth=1, relief="solid", padx=5, pady=5)
pet_frame6.grid(row=2, column=2, padx=10, pady=10)
pet_image_label6 = tk.Label(pet_frame6, image=pet6_photo, borderwidth=1)
pet_image_label6.grid(row=0, column=0, pady=(0, 5))
pet_label6 = tk.Label(pet_frame6, text="Cleo")
pet_label6.grid(row=1, column=0, pady=(0, 5))
details_button6 = tk.Button(pet_frame6, text="View Details", command=lambda: open_pet_details(6))
details_button6.grid(row=2, column=0)

# Exit button to close the application
exit_button = tk.Button(main_window, text="Exit", command=main_window.quit)
exit_button.grid(row=4, column=1, pady=20)

main_window.mainloop() # Starts loop