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

		self.i_point  = RegularPolygon(3,start_angle=  PI/2, color=PINK, fill_opacity=1).scale(0.2)
		self.i_point.generate_target()
		self.j_point  = RegularPolygon(3,start_angle= -PI/2, color=PINK, fill_opacity=1).scale(0.2)
		self.j_point.generate_target()
		self.pivot_text = TextMobject("Pivot", color=YELLOW).scale(1.1)

		self.partition_1()
		self.partition_2()
		self.partition_3()
		self.partition_4()
		self.partition_5()
		self.partition_6()
		self.partition_7()
		self.partition_8()
		self.partition_9()
		self.partition_10()
		self.partition_11()
		self.partition_12()
		self.partition_13()
		self.partition_14()
		self.partition_15()

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

	def partition_1(self):
		self.showAllPointers(self.boxes[0], self.boxes[9], '7', self.numbers[7])
		self.pivotMoreThanI('3')
		self.pivotMoreThanI('4')
		self.pivotLessThanI('9')
		self.pivotLessThanJ('8')
		self.pivotMoreThanJ('6')
		self.swap_ij('9', '6', self.numbers[9], self.numbers[6])
		self.pivotMoreThanI('1')
		self.pivotLessThanI('7')
		self.pivotMoreThanJ('2')
		self.swap_ij('7', '2', self.numbers[7], self.numbers[2])
		self.pivotMoreThanI('0')
		self.pivotMoreThanI('5')
		self.pivotLessThanI('7')
		self.pivotMoreThanJ('5')
		self.stopPartition(self.numbers[7])

	def partition_2(self):
		self.showAllPointers(self.boxes[0], self.boxes[6], '1', self.numbers[1])
		self.pivotLessThanI('3')
		self.pivotLessThanJ('5')
		self.pivotMoreThanJ('0')
		self.swap_ij('3', '0', self.numbers[3], self.numbers[0])
		self.pivotLessThanI('4')
		self.pivotLessThanJ('2')
		self.pivotMoreThanJ('1')
		self.swap_ij('4', '1', self.numbers[4], self.numbers[1])
		self.pivotLessThanI('6')
		self.pivotLessThanJ('6')
		self.pivotMoreThanJ('1')
		self.stopPartition(self.numbers[1])

	def partition_3(self):
		self.showAllPointers(self.boxes[0], self.boxes[1], '0', self.numbers[0])
		self.pivotLessThanI('0')
		self.pivotLessThanJ('1')
		self.pivotMoreThanJ('0')
		self.stopPartitionAndDeactivate(self.numbers[0], self.boxes[0], self.numbers[0])

	def partition_4(self):
		self.deactivateBox(self.numbers[1], self.boxes[1])

	def partition_5(self):
		self.showAllPointers(self.boxes[2], self.boxes[6], '2', self.numbers[2])
		self.pivotLessThanI('6')
		self.pivotLessThanJ('5')
		self.pivotLessThanJ('3')
		self.pivotMoreThanJ('2')
		self.swap_ij('6', '2', self.numbers[6], self.numbers[2])
		self.pivotLessThanI('4')
		self.pivotLessThanJ('4')
		self.pivotMoreThanJ('2')
		self.stopPartitionAndDeactivate(self.numbers[2], self.boxes[2], self.numbers[2])

	def partition_6(self):
		self.showAllPointers(self.boxes[3], self.boxes[6], '6', self.numbers[6])
		self.pivotMoreThanI('4')
		self.pivotLessThanI('6')
		self.pivotMoreThanJ('5')
		self.swap_ij('6', '5', self.numbers[6], self.numbers[5])
		self.pivotMoreThanI('3')
		self.pivotLessThanI('6')
		self.pivotMoreThanJ('3')
		self.stopPartition(self.numbers[6])

	def partition_7(self):
		self.showAllPointers(self.boxes[3], self.boxes[5], '5', self.numbers[5])
		self.pivotMoreThanI('4')
		self.pivotLessThanI('5')
		self.pivotMoreThanJ('3')
		self.swap_ij('5', '3', self.numbers[5], self.numbers[3])
		self.pivotLessThanI('5')
		self.pivotMoreThanJ('3')
		self.stopPartition(self.numbers[5])

	def partition_8(self):
		self.showAllPointers(self.boxes[3], self.boxes[4], '4', self.numbers[4])
		self.pivotLessThanI('4')
		self.pivotMoreThanJ('3')
		self.swap_ij('4', '3', self.numbers[4], self.numbers[3])
		self.pivotLessThanI('4')
		self.pivotMoreThanJ('3')
		self.stopPartitionAndDeactivate(self.numbers[3], self.boxes[3], self.numbers[4])

	def partition_9(self):
		self.deactivateBox(self.numbers[4], self.boxes[4])

	def partition_10(self):
		self.deactivateBox(self.numbers[5], self.boxes[5])

	def partition_11(self):
		self.deactivateBox(self.numbers[6], self.boxes[6])

	def partition_12(self):
		self.showAllPointers(self.boxes[7], self.boxes[9], '9', self.numbers[9])
		self.pivotMoreThanI('7')
		self.pivotLessThanI('9')
		self.pivotMoreThanJ('8')
		self.swap_ij('9', '8', self.numbers[9], self.numbers[8])
		self.pivotLessThanI('9')
		self.pivotMoreThanJ('8')
		self.stopPartition(self.numbers[9])

	def partition_13(self):
		self.showAllPointers(self.boxes[7], self.boxes[8], '7', self.numbers[7])
		self.pivotLessThanI('7')
		self.pivotLessThanJ('8')
		self.pivotMoreThanJ('7')
		self.stopPartitionAndDeactivate(self.numbers[7], self.boxes[7], self.numbers[7])

	def partition_14(self):
		self.deactivateBox(self.numbers[8], self.boxes[8])

	def partition_15(self):
		self.deactivateBox(self.numbers[9], self.boxes[9])

	def stopPartition(self, num):
		self.play(
			FadeOut(self.i_point),
			FadeOut(self.j_point),
			FadeToColor(num, WHITE),
		)

	def stopPartitionAndDeactivate(self, num, box, pivot_num):
		self.stopPartition(pivot_num)
		self.deactivateBox(num, box)

	def deactivateBox(self, num, box):
		self.play(
			FadeToColor(num, GREY),
			FadeToColor(box, GREY),
		)

	def swap_ij(self, i_val, j_val, i_num, j_num):
		swap_text = TexMobject("\\text{Swap }", i_val, "\\text{ with }", j_val).move_to(2 * DOWN)
		self.play(Write(swap_text))
		self.play(Swap(i_num, j_num))
		self.play(FadeOut(swap_text))
		self.shift_ij()

	def pivotMoreThanI(self, val):
		text = TexMobject("\\text{ }\\textgreater\\text{ }" + val)
		self.pivot_text.next_to(text, LEFT)
		comparison = VGroup(self.pivot_text, text).next_to(self.i_point, DOWN)
		self.play(Write(comparison))
		self.play(FadeOut(comparison))
		self.shift_i()

	def pivotLessThanI(self, val) :
		text = TexMobject("\\leq" + val)
		self.pivot_text.next_to(text, LEFT)
		comparison = VGroup(self.pivot_text, text).next_to(self.i_point, DOWN)
		self.play(Write(comparison))
		self.play(FadeOut(comparison))

	def pivotLessThanJ(self, val):
		text = TexMobject("\\text{ }\\textless\\text{ }" + val)
		self.pivot_text.next_to(text, LEFT)
		comparison = VGroup(self.pivot_text, text).next_to(self.j_point, UP)
		self.play(Write(comparison))
		self.play(FadeOut(comparison))
		self.shift_j()

	def pivotMoreThanJ(self, val):
		text = TexMobject("\\geq" + val)
		self.pivot_text.next_to(text, LEFT)
		comparison = VGroup(self.pivot_text, text).next_to(self.j_point, UP)
		self.play(Write(comparison))
		self.play(FadeOut(comparison))

	def shift_i(self):
		self.i_point.generate_target()
		self.i_point.target.shift(RIGHT)
		self.play(MoveToTarget(self.i_point))

	def shift_j(self):
		self.j_point.generate_target()
		self.j_point.target.shift(LEFT)
		self.play(MoveToTarget(self.j_point))

	def shift_ij(self):
		self.i_point.generate_target()
		self.i_point.target.shift(RIGHT)
		self.j_point.generate_target()
		self.j_point.target.shift(LEFT)
		self.play(
			MoveToTarget(self.i_point),
			MoveToTarget(self.j_point)
		)

	def showAllPointers(self, box_low, box_high, val, num):
		self.i_point.next_to(box_low, DOWN)
		self.j_point.next_to(box_high, UP)
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