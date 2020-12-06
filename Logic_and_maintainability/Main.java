import java.util.*;
class Main{
public static void main(String[] args) {
	List<File> files = new ArrayList<>();

	File f1 = new File("harshith", 100, "05-27-2020","05-27-2020", false, null);
	File f2 = new File("vinay", 10, "05-17-2020", "05-20-2020", false, null);
	File f3 = new File("ranjith", 50, "05-07-2020", "05-17-2020", false, null);
	File f4 = new File("jali", 1, "05-01-2020", "05-17-2020", false, null);

	files.add(f1);
	files.add(f2);
	files.add(f3);
	files.add(f4);
	File d2 = new File("101", 161, "05-27-2020","05-27-2020", false, files);
	// System.out.println(f1.name);
	File f5 = new File("koushik", 60, "05-27-2020","05-27-2020", false, null);
	List<File> files_2 = new ArrayList<>();
	files_2.add(f5);
	File d1 = new File("116", 167, "05-27-2020","05-27-2020", false, files_2);
	Directory d = new Directory(files);
	List<File> res = d.greaterThan(30);
	for (File f: res){
	System.out.println(f.name);	
	}
	
}
}