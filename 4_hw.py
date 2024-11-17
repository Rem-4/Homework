#1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle1 = Rectangle(2, 4)
rectangle2 = Rectangle(5, 6)
rectangle3 = Rectangle(7, 8)

print("Площадь первого прямоугольника:", rectangle1.area())
print("Периметр первого прямоугольника:", rectangle1.perimeter())

print("\nПлощадь второго прямоугольника:", rectangle2.area())
print("Периметр второго прямоугольника:", rectangle2.perimeter())

print("\nПлощадь третьего прямоугольника:", rectangle3.area())
print("Периметр третьего прямоугольника:", rectangle3.perimeter())

#2
class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        if self.b == 0:
            print("\nОшибка, делить на 0 нельзя!")
        else:
            return self.a / self.b
    def subtraction(self):
        return self.a - self.b
Numbers = Math(2, 4)

print("\nСумма:", Numbers.addition())
print("\nПроизведение:", Numbers.multiplication())
print("\nЧастное:", Numbers.division())
print("\nРазность:", Numbers.subtraction())

#3
class Button:
    def __init__(self, text, type, loc) -> str:
        self.text = text
        self.type = "Кнопка"
        self.loc = ""

    def click(self):
        print("Клик по кнопке " + self.text)
Text_Box_Button = Button("Text Box", "Кнопка", "")
Check_Box_Button = Button("Check Box", "Кнопка", "")
Radio_Button_Button = Button("Radio Button", "Кнопка", "")
Web_Tables_Button = Button("Web Tables", "Кнопка", "")
Buttons_Button = Button("Buttons", "Кнопка", "")
Links_Button = Button("Links", "Кнопка", "")
Broken_Links_Images_Button = Button("Broken Links - Images", "Кнопка", "")
Upload_and_Download_Button = Button("Upload and Download", "Кнопка", "")
Dynamic_Properties_Button = Button("Dynamic Properties", "Кнопка", "")

print("Текст кнопки: Text_Box_Button")
print("Текст кнопки: Check_Box_Button")
print("Текст кнопки: Radio_Button_Button")
print("Текст кнопки: Web_Tables_Button")
print("Текст кнопки: Links_Button")
print("Текст кнопки: Broken_Links_Images_Button")
print("Текст кнопки: Broken_Links_Images_Button")
print("Текст кнопки: Upload_and_Download_Button")
print("Текст кнопки: Dynamic_Properties_Button")
print("\n")

Text_Box_Button.click()
Check_Box_Button.click()
Radio_Button_Button.click()
Web_Tables_Button.click()
Buttons_Button.click()
Links_Button.click()
Broken_Links_Images_Button.click()
Upload_and_Download_Button.click()
Dynamic_Properties_Button.click()