mcd(){

	mkdir -p "$1" # -p stands no error if the directory already exists. 
	# $1 stands for cmd line argument 1. 
	cd "$1"
}
