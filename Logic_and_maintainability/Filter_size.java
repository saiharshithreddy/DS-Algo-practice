class Filter_size implements SizeCriteria{
	List<File> files_greater = new ArrayList<>();
	List<File> files_lesser = new ArrayList<>();
	List<File> files = new ArrayList<>();
	Filter_size(List<File> files){
		this.files = files;
	}

	public List<File> greaterthan(int size){

		for(File file: this.files){
			if (file.isDirectory == true){
				return greaterThan(size);
			}
			if (file.size > size){
				this.files_greater.add(file);
			3			

		}
		return files_greater;
	}

	public List<File> LesserThan(int size){
		
		for(File file: this.files){
			if (file.isDirectory == true){
				return LesserThan(size);
			}
			if (file.size < size){
				this.files_lesser.add(file);
			}
			

		}
		return files_lesser;
	}
}
