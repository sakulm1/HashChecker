# SHA-1 Hash Cracker with GUI

This readme was generated with chatgpt (what a fucking disgrace)

## Overview

This Python tool provides a graphical user interface (GUI) to perform brute-force attacks on SHA-1 hashes. It's designed to generate all possible combinations of a predefined character set to find the original input of a given SHA-1 hash. This project was developed as a potential solution for a university assignment, focusing on understanding the vulnerabilities and weaknesses of unsalted SHA-1 hashed passwords.

## Assignment Context

The assignment revolves around a web platform where users log in using a username and a password, with the password being no longer than 6 characters. The server maintains a list of usernames and corresponding SHA-1 hashed passwords. The website employs an insecure method for password storage: it stores a value determined by the "sha1" function applied to the password. The SHA-1 function returns a value of consistent byte length, represented in hexadecimal in the table.

Even though SHA-1 hashes cannot be "reversed" to reveal the original input directly, knowing the hash table allows for the possibility of determining the original passwords.

## Tool Description

### Key Components

1. **hashCreator Class:**
   - Generates passwords and their hashes, checking if generated hashes match provided hashes.
   - Controls the start and end of the brute-force process.
   - Generates combinations of strings and checks if their hash matches any target hashes.

2. **App Class:**
   - Creates and manages the GUI of the tool.
   - Provides widgets for user interaction and data input/output.
   - Interacts with the `hashCreator` class to control and display the brute-force process.

### Functionality

- **User Interaction:**
  - Set a maximum password length to be generated.
  - Input a list of SHA-1 hashes to attempt to crack.
  - Control the brute-force process with Start and Stop buttons.
  - View found passwords and their hashes.
  - View all generated passwords and their hashes in the output area.

- **Brute-Force Process:**
  - Generates all possible string combinations up to the user-defined maximum length and calculates their SHA-1 hash.
  - If a generated hash matches a target hash, the password and hash are displayed in the GUI.
  - The process can be stopped by the user at any time.

### Usage

1. **Set Maximum Password Length:**
   - Define the maximum length of the passwords to be generated.

2. **Input Target Hashes:**
   - Enter the SHA-1 hashes you aim to crack.

3. **Start Brute-Force:**
   - Begin the brute-force process and observe the output and found passwords.

4. **Stop Process:**
   - Halt the brute-force process at any time.

## Ethical and Legal Notice

This tool is intended for educational purposes only, to demonstrate the vulnerabilities of using unsalted SHA-1 hashes for password storage. Always respect privacy and legal standards. Never attempt to crack hashes or passwords without explicit permission.

## Future Improvements

- Implementing multi-threading for enhanced performance.
- Adding support for different hashing algorithms.
- Enhancing the GUI for a better user experience.

## Conclusion

Understanding the vulnerabilities of hashing algorithms and the importance of secure password storage is crucial in cybersecurity. This tool serves as an educational resource to explore and understand the implications of brute-force attacks on weak and unsalted hashes. Always ensure to follow ethical guidelines and legal requirements when dealing with cybersecurity practices.
