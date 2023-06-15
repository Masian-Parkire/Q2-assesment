
//**Ancestral Stories:** In many African cultures, the art of storytelling is passed
//down from generation to generation. Imagine you're creating an application that
//records these oral stories and translates them into different languages. The
//stories vary by length, moral lessons, and the age group they are intended for.
//Think about how you would model `Story`, `StoryTeller`, and `Translator`
//objects, and how inheritance might come into play if there are different types of
//stories or storytellers.
fun main() {
    val story1 = AncestralStory("long", "Obey your parents", "children", "The Hare and the Hyena")
    println(story1)
    val story2 = Story("The Ogre", "short")
    println(story2.recordStory())
    val story3 = StoryTeller("Mzee")
    println(story3.getStoryteller())
    val story4 = Translator("Kikuyu", "English")
    println(story4.translateStory())

    val prod1 = Product("Orange")
    println(prod1.calculateTotal(35, 7))

    val prod2 = Product("Socks")
    println(prod2.calculateTotal(300, 9))

    val prod3 = Product("Pen")
    println(prod3.calculateTotal(40, 10))

    val prod4 = Product("Bread")
    println(prod4.calculateTotal(65, 3))
}


open class AncestralStory(val length: String, val lessons: String, val agegroup: String, val title: String)

class Story(title: String, length: String) : AncestralStory(length, "Love your neighbour", "children", title) {
    fun recordStory(): String {
        return "This story is called $title"
    }
}

class StoryTeller(val narrator: String) : AncestralStory("two hours", "Do not lie", "Teenagers", "The ogre") {
    fun getStoryteller(): String {
        return "This story will be narrated by $narrator"
    }
}

class Translator(val languageOne: String, val languageTwo: String) : AncestralStory("1 hour", "Do not be greedy", "Youth", "The Hyena") {
    fun translateStory(): String {
        return "Translate this story from $languageOne to $languageTwo"
    }
}


//Create a class called Product with attributes for name, price, and quantity.
//Implement a method to calculate the total value of the product (price * quantity).
//Create multiple objects of the Product class and calculate their total values.
class Product( val name: String) {
    fun calculateTotal(price: Int, quantity: Int): Int {
        return price * quantity
    }
}