
public class Dog extends Animal{
    public String breed;

    public Dog(String name, int age, String breed){
        super(name,age);
        this.breed = breed;
    }

    @Override 
    public void Sound(){
        System.out.println("Woof");
    }
}
