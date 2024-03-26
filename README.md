# Gate Security System with Facial Recognition

This Python script implements a gate security system utilizing facial recognition technology. It authorizes personnel to enter the gate based on stored facial encodings and records their attendance in a MySQL database.

## Overview

This project provides a comprehensive solution for gate security, combining image processing, facial recognition, and database management. It offers the following features:

- **MySQL Database Integration**: Personnel information such as ID, force number, name, age, residency status, and address are stored in a MySQL database.
- **Real-time Facial Recognition**: Utilizes the `face_recognition` library to recognize personnel faces in real-time using a webcam feed.
- **Attendance Logging**: Records the attendance of recognized personnel in a CSV file (`Attendance.csv`), including timestamps.
- **Easy Deployment**: Simple setup and usage instructions enable quick deployment of the security system.

## Usage

1. Ensure a MySQL database is set up and configured. Modify the database connection parameters in the script if necessary.
2. Run the Python script (`main.py`) in your terminal or command prompt.
3. Follow the on-screen prompts to interact with the system.
4. View attendance records in the `Attendance.csv` file generated by the system.

## Dependencies

- `mysql-connector-python`: For MySQL database connectivity.
- `opencv-python`: For webcam access and image manipulation.
- `face-recognition`: For facial recognition capabilities.
- `numpy`: For numerical operations.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- The project relies on the following libraries: `mysql-connector-python`, `opencv-python`, `face-recognition`, and `numpy`.
- Special thanks to the contributors who helped enhance the project.

## Author

[Your Name](https://github.com/yourusername)


## Credits

- [face_recognition](https://github.com/ageitgey/face_recognition) library for facial recognition.
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) for MySQL database connectivity.

## Example

![Gate Security System Demo](demo.png)



## Credits

- [face_recognition](https://github.com/ageitgey/face_recognition) library for facial recognition.
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) for MySQL database connectivity.

## Example

![Gate Security System Demo](demo.png)

