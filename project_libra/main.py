import sys
import libra

def run(argv):
    libra.compare_images(argv[1], argv[2])
    

# Run the function if this is the main file executed
if __name__ == "__main__":
    run(sys.argv)