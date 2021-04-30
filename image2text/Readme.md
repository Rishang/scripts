# Extract Text from Images

**Requirements:**

1. Tesseract OCR

2. packages present in requirements.txt (`pip install -r requirements.txt`)

## Usage

    ❯ python img2txt.py --help

    Usage: img2txt.py [OPTIONS]

    Options:
    -p TEXT  Path of images.
    -o TEXT  Output path where text file will be stored. Default set to current
            directory

    --help   Show this message and exit.

### Examples

#### Single file

This will analyse `./example.jpg` and save the output text as `example.txt` at `dir/example.txt` directory

    python img2txt.py -p ./example.jpg -o ./dir

#### Multile file

For analysing multiple just define directory path where all images are present in `-p` and the outuput path `-o` where all text file will be saved

    python img2txt.py -p ./images -o ./m_txt

This is find all images in `./images` and save text output of all files to `./m_txt`
