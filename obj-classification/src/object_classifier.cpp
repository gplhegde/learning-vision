#include <opencv2/core/core.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <options.h>
#include <stdlib.h>

void print_help(char *app) {
	std::cout << "------------------------------------" << std::endl;
	std::cout << "Usage:" << endl;
	std::cout << app;
	std::cout << "-net <.prototxt specification for the network>"
	std::cout << " -model <.caffemodel file for the network>";
	std::cout << " -mean <mean image file>";
	std::cout << " -label <wordnet label file>";
	std::cout << " -mode <mode(available modes are image and video)>";
	std::cout << " [-img] <image path - required for mode = image>";
	std::cout << "------------------------------------" << std::endl;
}

int main(int argc, char **argv) {
	std::string model_path, net_path, mode, img_path, mean_path, label_path;

	if(argc < 6) {
		print_help(argv[0]);
		exit(1);
	}

	Options options(argc, argv);

	net_path = options.get<std::string>("net");
	model_path = options.get<std::string>("model");
	mean_path = options.get<std::string>("mean");
	label_path = options.get<std::string>("label");

	if(!options.has("mode")) {
		std::cout << "Please specify the application mode(sample OR test)" << std::endl;
		exit(1);
	} else {
		mode = options.get<string>("mode");
	}

	if(mode.compare("image") == 0) {
		if(options.has("img")) {
			img_path = options.get<std::string>("img");
		} else {
			cout << "Please specify image path" << endl;
			exit(1);
		}
	} else {
		std::cerr << "Only image mode is supported" << std::endl;
	}
	Mat input_img = cv::imread(img_path);

	cv::namedWindow("Input-image", CV_WINDOW_AUTOSIZE);
	cv::imshow("Input-image", input_img);

	cv::waitKey(0);
}
