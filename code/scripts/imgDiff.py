import sys
from PIL import Image
import numpy as np
import cv2


def compareImgs(img_a, img_b, threshold, bkg_color):
    
  	# Check if dimensions are the same
	if ( (img_a.width != img_b.width) or (img_a.height != img_b.height) ):
		print("image dimensions are different")
		return None

	# Create a new image
	imgOut   = Image.new(mode="RGBA", size=(img_a.width, img_a.height))
	imgOut_r = Image.new(mode="RGBA", size=(img_a.width, img_a.height))
	imgOut_g = Image.new(mode="RGBA", size=(img_a.width, img_a.height))
	imgOut_b = Image.new(mode="RGBA", size=(img_a.width, img_a.height))

	# Get different channels for image
	red_a, green_a, blue_a = img_a.split()
	red_b, green_b, blue_b = img_b.split()

	# Metrics to compute
	diffCount = 0 # number of different pixels

	numBins = 256
	histogram_r = np.zeros(numBins)
	histogram_g = np.zeros(numBins)
	histogram_b = np.zeros(numBins)


  	# Iterate over pixels
	index = 0
	for x in range( int(img_a.width) ):
		for y in range( int(img_a.height) ):
			

			#print(x,y)
			pixel_a = img_a.getpixel((x,y)) 
			pixel_b = img_b.getpixel((x,y)) 
			pixel_diff = abs( pixel_a[0]-pixel_b[0]) + abs( pixel_a[1]-pixel_b[1]) + abs( pixel_a[2]-pixel_b[2])
   
			if pixel_diff > threshold:
				# num of different pixels
				diffCount = diffCount + 1

				# amount of difference per color
				diff_r = abs( red_a.getpixel((x,y))   - red_b.getpixel((x,y)) )
				diff_g = abs( green_a.getpixel((x,y)) - green_b.getpixel((x,y)) )
				diff_b = abs( blue_a.getpixel((x,y))  - blue_b.getpixel((x,y)) )

				histogram_r[diff_r] = histogram_r[diff_r] + 1
				histogram_g[diff_g] = histogram_g[diff_g] + 1
				histogram_b[diff_b] = histogram_b[diff_b] + 1

				# Create new pixels
				change_amount = int( (diff_r + diff_g + diff_b)/3 )
				highlight_color= (128, change_amount,change_amount, 255)
				imgOut.putpixel( (x,y), highlight_color)

				imgOut_r.putpixel( (x,y), (diff_r,diff_r,diff_r, 255)) 
				imgOut_g.putpixel( (x,y), (diff_g,diff_g,diff_g, 255)) 
				imgOut_b.putpixel( (x,y), (diff_b,diff_b,diff_b, 255)) 

			else:   # image same
				# Create new pixels
				imgOut.putpixel( (x,y), bkg_color) # transparent
				imgOut_r.putpixel( (x,y), bkg_color) 
				imgOut_g.putpixel( (x,y), bkg_color) 
				imgOut_b.putpixel( (x,y), bkg_color) 

				histogram_r[0] = histogram_r[0] + 1
				histogram_g[0] = histogram_g[0] + 1
				histogram_b[0] = histogram_b[0] + 1

			index = index+1
			if (index >= ( 0.05* ( int(img_a.width)*int(img_a.height) ) )):
				index = 0
				print("-", end='', flush=True)
    
	return imgOut, imgOut_r, imgOut_g, imgOut_b, diffCount, histogram_r, histogram_g, histogram_b


def main(img_orig, img_comp, threshold, col):
    # Open Images
	img_a = Image.open(img_orig)
	img_b = Image.open(img_comp)
 
	# Compare
	img_out, img_out_r, img_out_g, img_out_b, diffCount, hist_r, hist_b, hist_g = compareImgs(img_a, img_b, threshold, col)
 
	# Create output images
	new_name = img_comp[:-4] + "_" + str(threshold)
	img_out.save(new_name + "_diff.png", format="png")
	img_out_r.save(new_name + "_red_diff.png", format="png")
	img_out_g.save(new_name + "_green_diff.png", format="png")
	img_out_b.save(new_name + "_blue_diff.png", format="png")
 
	# Do an image equalization to highlight differences
	img = cv2.imread(new_name + "_diff.png",0)
	equ = cv2.equalizeHist(img)
	cv2.imwrite(new_name + "_eq_diff.png",equ)
 
	# Save histograms
	np.savetxt(new_name + "_red_hist.csv", hist_r, delimiter=",")
	np.savetxt(new_name + "_green_hist.csv", hist_g, delimiter=",")
	np.savetxt(new_name + "_blue_hist.csv", hist_b, delimiter=",")
 
	print("\nNumber of different pixels: ", diffCount,  ", ", float(diffCount/(img_a.width * img_a.height)) ," of the ofiginal image.")
 
 

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print("Run sciprt as: python imageDiff.py <original_img> <comparison_img> <threshold> <optional: background col as R G B>")
        exit(0)
    
    threshold = 0
    if len(sys.argv) >= 4:
        threshold = int(sys.argv[3])
        
    bkgColor = (0,0,0, 0)
    if len(sys.argv) == 7:
       bkgColor = ( int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]),  255) 
       
    # Output input to verify
    print("Original image: ", sys.argv[1])
    print("Comparison image: ", sys.argv[1])
    print("Pixel threshold: ", threshold)
    print("Background Color: ", bkgColor[0], bkgColor[1], bkgColor[2])
    
    main(sys.argv[1], sys.argv[2], threshold, bkgColor)
    
    
# Why did I write this?
#  No one can detect a change in difference of 1 pixel, now we should be able to see how different the images are

# Run as:
# python imgDiff.py a.png b.png 1 0 0 0
