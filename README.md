# Email Parser

Parse email files and extract following information from those file.
- To
- From
- Subject
- Body (text/html)
- Time 
- Attachments 

Running the **email_parser.py** file will generate a csv file named **data.csv** containing the email metadata mentioned above.
The emails folder contains the email files. The **data.csv** is generated from the email files from the **emails**  folder. 
So. to add extract new emails just add the email(.eml file) to the folder.

## Requirements

- Python 3.6 or higher
## Installation

- Clone the repository.
```
git clone https://github.com/ihasidul/email-metadata-extractor
```
- Run the script:
```
python email_parser.py
```

