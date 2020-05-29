
import java.util.*;
class File{
	private String name;
	private int size;
	private boolean isDirectory;
	private String creationDate;
	private String modifiedDate;
	private List<File> files;

	File(String name, int size,  String creationDate, String modifiedDate, boolean isDirectory, List<File> files){
		this.name = name;
		this.size = size;
		this.isDirectory = isDirectory;
		this.creationDate = creationDate;
		this.modifiedDate = modifiedDate;
		this.files = files;
	}
	public String get_name(){
		return this.name

	}
	public void set_name(String name){
		this.name = name
	}
}


