from manimlib.imports import *

class Demo(Scene):
	def construct(self):
		self.showArray()
		self.doSort()

	def showArray(self):
		boxes = []

		for i in range(10):
			boxes.append(
				Square(side_length=1.0, color=BLUE_C).move_to(4.5 * LEFT + i * RIGHT)
			)

		numbers = []

		for i in range(10):
			numbers.append(
				TextMobject(str(i))
			)

		numbers[3].move_to(boxes[0].get_center())
		numbers[4].move_to(boxes[1].get_center())
		numbers[9].move_to(boxes[2].get_center())
		numbers[1].move_to(boxes[3].get_center())
		numbers[7].move_to(boxes[4].get_center())
		numbers[0].move_to(boxes[5].get_center())
		numbers[5].move_to(boxes[6].get_center())
		numbers[2].move_to(boxes[7].get_center())
		numbers[6].move_to(boxes[8].get_center())
		numbers[8].move_to(boxes[9].get_center())

		self.play(
			AnimationGroup(
				ShowCreation(boxes[0]),
				ShowCreation(boxes[1]),
				ShowCreation(boxes[2]),
				ShowCreation(boxes[3]),
				ShowCreation(boxes[4]),
				ShowCreation(boxes[5]),
				ShowCreation(boxes[6]),
				ShowCreation(boxes[7]),
				ShowCreation(boxes[8]),
				ShowCreation(boxes[9]),
				lag_ratio=0.2
			)
		)

		self.play(
			AnimationGroup(
				Write(numbers[0]),
				Write(numbers[1]),
				Write(numbers[2]),
				Write(numbers[3]),
				Write(numbers[4]),
				Write(numbers[5]),
				Write(numbers[6]),
				Write(numbers[7]),
				Write(numbers[8]),
				Write(numbers[9]),
				lag_ratio=0.2
			)
		)

		self.boxes = boxes
		self.numbers = numbers

		self.array = VGroup(VGroup(*self.boxes), VGroup(*self.numbers))

		brace = Brace(self.array, DOWN)
		brace_text = brace.get_text("array A")

		self.play(
			GrowFromCenter(brace),
			Write(brace_text),
		)

		self.wait()

		self.play(
			FadeOut(brace),
			FadeOut(brace_text),
		)

	def doSort(self):
		array = self.array
		array.generate_target()
		array.target.shift(UP)

		self.play(MoveToTarget(array))

		self.i_point = RegularPolygon(3,start_angle= PI/2, color=PINK, fill_opacity=1).scale(0.2)

		self.j_point = RegularPolygon(3,start_angle=-PI/2, color=PINK, fill_opacity=1).scale(0.2)

		self.pivot_text = TextMobject("Pivot", color=YELLOW).scale(1.1)

		self.pivot_1()
		self.pivot_2()
		self.pivot_3()
		self.pivot_4()
		self.pivot_5()
		self.pivot_6()
		self.pivot_7()
		self.pivot_8()
		self.pivot_9()
		self.pivot_10()

		self.activateArray()

		array.generate_target()
		array.target.shift(DOWN)

		self.play(MoveToTarget(array))

		ordered = TextMobject("Sorted").move_to(UP)

		self.play(Write(ordered))

		self.wait(3)

		self.play(
			FadeOut(array),
			FadeOut(ordered),
		)

		self.wait(10)

	def pivot_1(self):
		self.showAllPointers(self.boxes[0], self.boxes[9], "8", self.numbers[8])

		self.greaterThanNoSwap("3")
		self.greaterThanNoSwap("4")
		self.lessThan("9")
		self.greaterThanSwap("9", "1", self.numbers[9], self.numbers[1])
		self.greaterThanSwap("9", "7", self.numbers[9], self.numbers[7])
		self.greaterThanSwap("9", "0", self.numbers[9], self.numbers[0])
		self.greaterThanSwap("9", "5", self.numbers[9], self.numbers[5])
		self.greaterThanSwap("9", "2", self.numbers[9], self.numbers[2])
		self.greaterThanSwap("9", "6", self.numbers[9], self.numbers[6])

		self.pivotDone("9", "8", self.numbers[9], self.numbers[8], self.boxes[8])

	def pivot_2(self):
		self.showAllPointers(self.boxes[0], self.boxes[7], "6", self.numbers[6])

		self.greaterThanNoSwap("3")
		self.greaterThanNoSwap("4")
		self.greaterThanNoSwap("1")
		self.lessThan("7")
		self.greaterThanSwap("7", "0", self.numbers[7], self.numbers[0])
		self.greaterThanSwap("7", "5", self.numbers[7], self.numbers[5])
		self.greaterThanSwap("7", "2", self.numbers[7], self.numbers[2])

		self.pivotDone("7", "6", self.numbers[7], self.numbers[6], self.boxes[6])

	def pivot_3(self):
		self.showAllPointers(self.boxes[0], self.boxes[5], "2", self.numbers[2])

		self.lessThan("3")
		self.lessThan("4")
		self.greaterThanSwap("3", "1", self.numbers[3], self.numbers[1])
		self.greaterThanSwap("4", "0", self.numbers[4], self.numbers[0])
		self.lessThan("5")

		self.pivotDone("3", "2", self.numbers[3], self.numbers[2], self.boxes[2])

	def pivot_4(self):
		self.showAllPointers(self.boxes[0], self.boxes[1], "0", self.numbers[0])

		self.lessThan("1")

		self.pivotDone("1", "0", self.numbers[1], self.numbers[0], self.boxes[0])

	def pivot_5(self):
		self.deactivateBox(self.numbers[1], self.boxes[1])

	def pivot_6(self):
		self.showAllPointers(self.boxes[3], self.boxes[5], "3", self.numbers[3])

		self.lessThan("4")
		self.lessThan("5")

		self.pivotDone("4", "3", self.numbers[4], self.numbers[3], self.boxes[3])

	def pivot_7(self):
		self.showAllPointers(self.boxes[4], self.boxes[5], "4", self.numbers[4])

		self.lessThan("5")

		self.pivotDone("5", "4", self.numbers[5], self.numbers[4], self.boxes[4])

	def pivot_8(self):
		self.deactivateBox(self.numbers[5], self.boxes[5])

	def pivot_9(self):
		self.deactivateBox(self.numbers[7], self.boxes[7])

	def pivot_10(self):
		self.deactivateBox(self.numbers[9], self.boxes[9])

	def showAllPointers(self, box_low, box_high, val, num):
		self.i_point.next_to(box_low, DOWN)
		self.j_point.next_to(box_low, UP)
		text = TexMobject("\\text{Choose }" + val + "\\text{ as }")
		self.pivot_text.next_to(text, RIGHT)
		choose_pivot = VGroup(text, self.pivot_text).move_to(2 * DOWN)

		self.play(
			Write(choose_pivot),
			FadeToColor(num, YELLOW),
		)

		self.play(
			Indicate(num),
		)

		self.play(
			FadeOut(choose_pivot),
			DrawBorderThenFill(self.i_point),
			DrawBorderThenFill(self.j_point),
		)

	def pivotDone(self, left_val, right_val, left_num, right_num, box):
		result = TexMobject("\\text{Swap }" + left_val + "\\text{ with }" + right_val).move_to(2 * DOWN)
		self.play(Write(result))
		self.play(Swap(left_num, right_num))
		self.play(
			FadeOut(result),
			FadeOut(self.i_point),
			FadeOut(self.j_point),
		)
		self.play(
			FadeToColor(box, GRAY),
			FadeToColor(right_num, GRAY),
		)

	def deactivateBox(self, num, box):
		self.play(
			FadeToColor(num, GRAY),
			FadeToColor(box, GRAY),
		)

	def lessThan(self, val):
		text = TexMobject("\\text{ }\\textless\\text{ }" + val)
		self.pivot_text.next_to(text, LEFT)
		comparison = VGroup(self.pivot_text, text).next_to(self.j_point, UP)

		self.play(Write(comparison))
		self.play(FadeOut(comparison))
		self.shift_j()

	def greaterThanNoSwap(self, val):
		text = TexMobject("\\geq" + val)
		self.pivot_text.next_to(text, LEFT)
		comparison = VGroup(self.pivot_text, text).next_to(self.j_point, UP)

		result = TextMobject("No need to swap").move_to(2 * DOWN)
		self.play(Write(comparison))
		self.play(Write(result), run_time=0.5)
		self.shift_i()
		self.play(FadeOut(comparison), FadeOut(result))
		self.shift_j()

	def greaterThanSwap(self, left_val, right_val, left_num, right_num):
		text = TexMobject("\\geq" + right_val)
		self.pivot_text.next_to(text, LEFT)
		comparison = VGroup(self.pivot_text, text).next_to(self.j_point, UP)

		result = TexMobject("\\text{Swap }" + left_val + "\\text{ with }" + right_val).move_to(2 * DOWN)
		self.play(Write(comparison))
		self.play(Write(result))
		self.play(Swap(left_num, right_num))
		self.shift_i()
		self.play(FadeOut(comparison), FadeOut(result))
		self.shift_j()

	def shift_i(self):
		self.i_point.generate_target()
		self.i_point.target.shift(RIGHT)

		self.play(MoveToTarget(self.i_point))

	def shift_j(self):
		self.j_point.generate_target()
		self.j_point.target.shift(RIGHT)

		self.play(MoveToTarget(self.j_point))

	def activateArray(self):
		self.play(
			AnimationGroup(
				FadeToColor(self.boxes[0], BLUE_C),
				FadeToColor(self.numbers[0], WHITE),
				FadeToColor(self.boxes[1], BLUE_C),
				FadeToColor(self.numbers[1], WHITE),
				FadeToColor(self.boxes[2], BLUE_C),
				FadeToColor(self.numbers[2], WHITE),
				FadeToColor(self.boxes[3], BLUE_C),
				FadeToColor(self.numbers[3], WHITE),
				FadeToColor(self.boxes[4], BLUE_C),
				FadeToColor(self.numbers[4], WHITE),
				FadeToColor(self.boxes[5], BLUE_C),
				FadeToColor(self.numbers[5], WHITE),
				FadeToColor(self.boxes[6], BLUE_C),
				FadeToColor(self.numbers[6], WHITE),
				FadeToColor(self.boxes[7], BLUE_C),
				FadeToColor(self.numbers[7], WHITE),
				FadeToColor(self.boxes[8], BLUE_C),
				FadeToColor(self.numbers[8], WHITE),
				FadeToColor(self.boxes[9], BLUE_C),
				FadeToColor(self.numbers[9], WHITE),
				lag_ratio=0.1
			)
		)
