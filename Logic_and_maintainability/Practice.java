import java.util.*;
import java.util.Map;
import java.util.HashMap;
class Practice{

	public static void main(String[] args) {
		LinkedList<Integer> files = new LinkedList<Integer>();
		files.add(1);
		files.add(2);
		files.add(3);
		files.add(2,20);
		files.remove(3);
		System.out.println(files);

		ArrayList<String> arr = new ArrayList<>();
		arr.add("20");
		System.out.println(arr);		

		HashMap<String, Integer> map = new HashMap<>();
		map.put("Harshith", 10);
		System.out.println(map.get("Harshith"));
	}
}


enum Vehicle{
	Small;
	Medium;
	High;
}

enum ParkingStatus{
	Occupied;
	Unoccupied;
	Under_repair;
}

class ParkingService{
	public Ticket entry(VehicleType type){

	}
	public double VehicleExit(long tickedId){

	}
}

class Ticket{
	long id;
	Date entryTime, exitTime;
	ParkingSlot slot;
	String VehicleNum;

}


