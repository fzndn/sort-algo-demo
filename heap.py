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
		self.showHierarchy()

		self.child_pointer  = RegularPolygon(3,start_angle= -PI/2, color=PINK, fill_opacity=1).scale(0.2)
		self.child_pointer.generate_target()
		self.parent_pointer = RegularPolygon(3,start_angle= -PI/2, color=PINK, fill_opacity=1).scale(0.2)
		self.parent_pointer.generate_target()

		self.heapify_1()
		self.pick(9, 4)
		self.heapify_2()
		self.pick(8, 1)
		self.heapify_3()
		self.pick(7, 1)
		self.heapify_4()
		self.pick(6, 3)
		self.heapify_5()
		self.pick(5, 0)
		self.heapify_6()
		self.pick(4, 1)
		self.heapify_7()
		self.pick(3, 0)
		self.heapify_8()
		self.pick(2, 1)
		self.heapify_9()
		self.pick(1, 0)

		self.activateBoxes()
		self.reconstructToArray()

		array = VGroup(*self.boxes, *self.numbers)

		ordered = TextMobject("Sorted").move_to(UP)
		self.play(Write(ordered))
		self.wait(3)
		self.play(
			FadeOut(array),
			FadeOut(ordered),
		)

		self.wait(10)

	def heapify_1(self):
		self.showParentPointer(self.boxes[9])
		self.moveParentPointer(self.boxes[8])
		self.moveParentPointer(self.boxes[7])
		self.moveParentPointer(self.boxes[6])
		self.moveParentPointer(self.boxes[5])
		self.moveParentPointer(self.boxes[4])
		self.onlyChildSwap(
			'7', '8',
			self.numbers[7], self.numbers[8],
			self.boxes[9]
		)
		self.moveParentPointer(self.boxes[3])
		self.leftChildGreaterRightChildGreatest(
			'1', '2', '6',
			self.numbers[1], self.numbers[6],
			self.boxes[7], self.boxes[8]
		)
		self.moveParentPointer(self.boxes[2])
		# Extract as a function
		self.child_pointer.next_to(self.boxes[5], UP)
		self.play(DrawBorderThenFill(self.child_pointer))
		comparison = TexMobject('0' + " \\leq " + '9').move_to(2.7 * DOWN)
		self.play(Write(comparison))
		self.play(FadeOut(comparison))
		self.child_pointer.target.next_to(self.boxes[6], UP)
		self.play(MoveToTarget(self.child_pointer))
		comparison = TexMobject('5' + " \\leq " + '9').move_to(2.7 * DOWN)
		self.play(Write(comparison))
		self.play(FadeOut(comparison), FadeOut(self.child_pointer))
		self.moveParentPointer(self.boxes[1])
		self.leftChildGreaterRightChildGreatest(
			'4', '6', '8',
			self.numbers[4], self.numbers[8],
			self.boxes[3], self.boxes[4]
		)
		self.moveParentPointer(self.boxes[4])
		self.onlyChildSwap(
			'4', '7',
			self.numbers[4], self.numbers[7],
			self.boxes[9]
		)
		self.moveParentPointer(self.boxes[0])
		self.leftChildGreaterRightChildGreatest(
			'3', '8', '9',
			self.numbers[3], self.numbers[9],
			self.boxes[1], self.boxes[2]
		)
		self.moveParentPointer(self.boxes[2])
		self.leftChildLessRightChildGreater(
			'3', '0', '5',
			self.numbers[3], self.numbers[5],
			self.boxes[5], self.boxes[6]
		)
		self.play(FadeOut(self.parent_pointer))

	def heapify_2(self):
		self.showParentPointer(self.boxes[0])
		self.rightChildGreaterLeftChildGreatest(
			'4', '8', '5',
			self.numbers[4], self.numbers[8],
			self.boxes[1], self.boxes[2]
		)
		self.moveParentPointer(self.boxes[1])
		self.leftChildGreaterRightChildGreatest(
			'4', '6', '7',
			self.numbers[4], self.numbers[7],
			self.boxes[3], self.boxes[4]
		)
		self.play(FadeOut(self.parent_pointer))

	def heapify_3(self):
		self.showParentPointer(self.boxes[0])
		self.rightChildGreaterLeftChildGreatest(
			'1', '7', '5',
			self.numbers[1], self.numbers[7],
			self.boxes[1], self.boxes[2]
		)
		self.moveParentPointer(self.boxes[1])
		self.rightChildGreaterLeftChildGreatest(
			'1', '6', '4',
			self.numbers[1], self.numbers[6],
			self.boxes[3], self.boxes[4]
		)
		self.moveParentPointer(self.boxes[3])
		self.onlyChildSwap(
			'1', '2',
			self.numbers[1], self.numbers[2],
			self.boxes[7]
		)
		self.play(FadeOut(self.parent_pointer))

	def heapify_4(self):
		self.showParentPointer(self.boxes[0])
		self.rightChildGreaterLeftChildGreatest(
			'1', '6', '5',
			self.numbers[1], self.numbers[6],
			self.boxes[1], self.boxes[2]
		)
		self.moveParentPointer(self.boxes[1])
		self.leftChildGreaterRightChildGreatest(
			'1', '2', '4',
			self.numbers[1], self.numbers[4],
			self.boxes[3], self.boxes[4]
		)
		self.play(FadeOut(self.parent_pointer))

	def heapify_5(self):
		self.showParentPointer(self.boxes[0])
		self.leftChildGreaterRightChildGreatest(
			'3', '4', '5',
			self.numbers[3], self.numbers[5],
			self.boxes[1], self.boxes[2]
		)
		self.moveParentPointer(self.boxes[2])
		self.onlyChildNoSwap(
			'3', '0',
			self.boxes[5]
		)
		self.play(FadeOut(self.parent_pointer))

	def heapify_6(self):
		self.showParentPointer(self.boxes[0])
		self.rightChildGreaterLeftChildGreatest(
			'0', '4', '3',
			self.numbers[0], self.numbers[4],
			self.boxes[1], self.boxes[2]
		)
		self.moveParentPointer(self.boxes[1])
		self.rightChildGreaterLeftChildGreatest(
			'0', '2', '1',
			self.numbers[0], self.numbers[2],
			self.boxes[3], self.boxes[4]
		)
		self.play(FadeOut(self.parent_pointer))

	def heapify_7(self):
		self.showParentPointer(self.boxes[0])
		self.leftChildGreaterRightChildGreatest(
			'1', '2', '3',
			self.numbers[1], self.numbers[3],
			self.boxes[1], self.boxes[2]
		)
		self.play(FadeOut(self.parent_pointer))

	def heapify_8(self):
		self.showParentPointer(self.boxes[0])
		self.rightChildGreaterLeftChildGreatest(
			'0', '2', '1',
			self.numbers[0], self.numbers[2],
			self.boxes[1], self.boxes[2]
		)
		self.play(FadeOut(self.parent_pointer))

	def heapify_9(self):
		self.showParentPointer(self.boxes[0])
		self.onlyChildNoSwap(
			'1', '0',
			self.boxes[1]
		)
		self.play(FadeOut(self.parent_pointer))

	def pick(self, maks, last):
		result = TextMobject("Swap ", str(last), " with ", str(maks)).move_to(2.7 * DOWN + 3.2 * RIGHT)
		self.play(Write(result))
		self.play(Swap(self.numbers[maks], self.numbers[last]))
		self.play(
			FadeToColor(self.boxes[maks], GREY),
			FadeToColor(self.numbers[maks], GREY),
			FadeOut(result)
		)

	def activateBoxes(self):
		self.play(
			AnimationGroup(
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

	def reconstructToArray(self):
		index_9 = VGroup(self.boxes[9], self.numbers[9])
		index_8 = VGroup(self.boxes[8], self.numbers[8])
		index_7 = VGroup(self.boxes[7], self.numbers[7])
		index_6 = VGroup(self.boxes[6], self.numbers[6])
		index_5 = VGroup(self.boxes[5], self.numbers[5])
		index_4 = VGroup(self.boxes[4], self.numbers[4])
		index_3 = VGroup(self.boxes[3], self.numbers[3])
		index_2 = VGroup(self.boxes[2], self.numbers[2])
		index_1 = VGroup(self.boxes[1], self.numbers[1])
		index_0 = VGroup(self.boxes[0], self.numbers[0])

		index_0.generate_target()
		index_1.generate_target()
		index_2.generate_target()
		index_3.generate_target()
		index_4.generate_target()
		index_5.generate_target()
		index_6.generate_target()
		index_7.generate_target()
		index_8.generate_target()
		index_9.generate_target()

		index_9.target.move_to(4.5 * RIGHT + 2.7 * DOWN)
		index_8.target.move_to(3.5 * RIGHT + 2.7 * DOWN)
		index_7.target.move_to(2.5 * RIGHT + 2.7 * DOWN)

		index_6.target.move_to(1.5 * RIGHT + 0.9 * DOWN)
		index_5.target.move_to(0.5 * RIGHT + 0.9 * DOWN)
		index_4.target.move_to(0.5 * LEFT  + 0.9 * DOWN)
		index_3.target.move_to(1.5 * LEFT  + 0.9 * DOWN)

		index_2.target.move_to(2.5 * LEFT  + 0.9 * UP)
		index_1.target.move_to(3.5 * LEFT  + 0.9 * UP)

		index_0.target.move_to(4.5 * LEFT  + 2.7 * UP)

		self.play(
			MoveToTarget(index_0),
			MoveToTarget(index_1),
			MoveToTarget(index_2),
			MoveToTarget(index_3),
			MoveToTarget(index_4),
			MoveToTarget(index_5),
			MoveToTarget(index_6),
			MoveToTarget(index_7),
			MoveToTarget(index_8),
			MoveToTarget(index_9),
		)

		row_2 = VGroup(index_1, index_2)
		row_3 = VGroup(index_3, index_4, index_5, index_6)
		row_4 = VGroup(index_7, index_8, index_9)

		row_2.generate_target()
		row_3.generate_target()
		row_4.generate_target()

		index_0.target.shift(2.7 * DOWN)
		row_2.target.shift(0.9 * DOWN)
		row_3.target.shift(0.9 * UP)
		row_4.target.shift(2.7 * UP)

		self.play(
			MoveToTarget(index_0),
			MoveToTarget(row_2),
			MoveToTarget(row_3),
			MoveToTarget(row_4),
		)

	def leftChildGreaterRightChildGreatest(self, parent_val, left_child_val, right_child_val, parent_num, right_child_num, left_child_box, right_child_box):
		self.child_pointer.next_to(left_child_box, UP)
		self.play(DrawBorderThenFill(self.child_pointer))
		comparison = TexMobject(left_child_val + "\\text{ } \\textgreater \\text{ }" + parent_val).move_to(2.7 * DOWN)
		self.play(Write(comparison))
		result = TextMobject("Choose ", left_child_val).move_to(2.7 * DOWN + 3.2 * RIGHT)
		self.play(Write(result))
		self.play(FadeOut(comparison))
		self.child_pointer.target.next_to(right_child_box, UP)
		self.play(MoveToTarget(self.child_pointer))
		comparison = TexMobject(right_child_val + "\\text{ } \\textgreater \\text{ }" + left_child_val).move_to(2.7 * DOWN)
		self.play(Write(comparison))
		self.play(Transform(result[1], TexMobject(right_child_val).next_to(result[0], RIGHT)))
		self.play(Swap(parent_num, right_child_num))
		self.play(FadeOut(comparison), FadeOut(result), FadeOut(self.child_pointer))

	def leftChildLessRightChildGreater(self, parent_val, left_child_val, right_child_val, parent_num, right_child_num, left_child_box, right_child_box):
		self.child_pointer.next_to(left_child_box, UP)
		self.play(DrawBorderThenFill(self.child_pointer))
		comparison = TexMobject(left_child_val + " \\leq " + parent_val).move_to(2.7 * DOWN)
		self.play(Write(comparison))
		self.play(FadeOut(comparison))
		self.child_pointer.target.next_to(right_child_box, UP)
		self.play(MoveToTarget(self.child_pointer))
		comparison = TexMobject(right_child_val + "\\text{ } \\textgreater \\text{ }" + parent_val).move_to(2.7 * DOWN)
		self.play(Write(comparison))
		result = TextMobject("Choose " + right_child_val).move_to(2.7 * DOWN + 3.2 * RIGHT)
		self.play(Write(result))
		self.play(Swap(parent_num, right_child_num))
		self.play(FadeOut(comparison), FadeOut(result), FadeOut(self.child_pointer))

	def rightChildGreaterLeftChildGreatest(self, parent_val, left_child_val, right_child_val, parent_num, left_child_num, left_child_box, right_child_box):
		self.child_pointer.next_to(left_child_box, UP)
		self.play(DrawBorderThenFill(self.child_pointer))
		comparison = TexMobject(left_child_val + "\\text{ } \\textgreater \\text{ }" + parent_val).move_to(2.7 * DOWN)
		self.play(Write(comparison))
		result = TextMobject("Choose ", left_child_val).move_to(2.7 * DOWN + 3.2 * RIGHT)
		self.play(Write(result))
		self.play(FadeOut(comparison))
		self.child_pointer.target.next_to(right_child_box, UP)
		self.play(MoveToTarget(self.child_pointer))
		comparison = TexMobject(right_child_val + " \\leq " + left_child_val).move_to(2.7 * DOWN)
		self.play(Write(comparison))
		self.play(Indicate(result[1]))
		self.play(Swap(parent_num, left_child_num))
		self.play(FadeOut(comparison), FadeOut(result), FadeOut(self.child_pointer))

	def onlyChildSwap(self, parent_val, child_val, parent_num, child_num, child_box):
		self.child_pointer.next_to(child_box, UP)
		self.play(DrawBorderThenFill(self.child_pointer))
		comparison = TexMobject(child_val + "\\text{ } \\textgreater \\text{ }" + parent_val).move_to(2.7 * DOWN)
		self.play(Write(comparison))
		result = TextMobject("Choose " + child_val).move_to(2.7 * DOWN + 3.2 * RIGHT)
		self.play(Write(result))
		self.play(Swap(parent_num, child_num))
		self.play(FadeOut(comparison), FadeOut(result), FadeOut(self.child_pointer))

	def onlyChildNoSwap(self, parent_val, child_val, child_box):
		self.child_pointer.next_to(child_box, UP)
		self.play(DrawBorderThenFill(self.child_pointer))
		comparison = TexMobject(child_val + " \\leq " + parent_val).move_to(2.7 * DOWN)
		self.play(Write(comparison))
		self.play(FadeOut(comparison), FadeOut(self.child_pointer))

	def showHierarchy(self):
		row_1 = VGroup(self.boxes[0], self.numbers[3])
		row_2 = VGroup(self.boxes[1], self.boxes[2], self.numbers[4], self.numbers[9])
		row_3 = VGroup(self.boxes[3], self.boxes[4], self.boxes[5], self.boxes[6],
			self.numbers[1], self.numbers[7], self.numbers[0], self.numbers[5])
		row_4 = VGroup(self.boxes[7], self.boxes[8], self.boxes[9],
			self.numbers[2], self.numbers[6], self.numbers[8])

		row_1.generate_target()
		row_2.generate_target()
		row_3.generate_target()
		row_4.generate_target()

		row_1.target.shift(2.7 * UP)
		row_2.target.shift(0.9 * UP)
		row_3.target.shift(0.9 * DOWN)
		row_4.target.shift(2.7 * DOWN)

		self.play(
			MoveToTarget(row_1),
			MoveToTarget(row_2),
			MoveToTarget(row_3),
			MoveToTarget(row_4),
		)

		index_0 = VGroup(self.boxes[0], self.numbers[3])
		index_1 = VGroup(self.boxes[1], self.numbers[4])
		index_2 = VGroup(self.boxes[2], self.numbers[9])
		index_3 = VGroup(self.boxes[3], self.numbers[1])
		index_4 = VGroup(self.boxes[4], self.numbers[7])
		index_5 = VGroup(self.boxes[5], self.numbers[0])
		index_6 = VGroup(self.boxes[6], self.numbers[5])
		index_7 = VGroup(self.boxes[7], self.numbers[2])
		index_8 = VGroup(self.boxes[8], self.numbers[6])
		index_9 = VGroup(self.boxes[9], self.numbers[8])

		index_0.generate_target()
		index_1.generate_target()
		index_2.generate_target()
		index_3.generate_target()
		index_4.generate_target()
		index_5.generate_target()
		index_6.generate_target()
		index_7.generate_target()
		index_8.generate_target()
		index_9.generate_target()

		index_0.target.move_to(2.7 * UP)
		index_1.target.move_to(0.9 * UP   + 3.2 * LEFT)
		index_2.target.move_to(0.9 * UP   + 3.2 * RIGHT)
		index_3.target.move_to(0.9 * DOWN + 4.8 * LEFT)
		index_4.target.move_to(0.9 * DOWN + 1.6 * LEFT)
		index_5.target.move_to(0.9 * DOWN + 1.6 * RIGHT)
		index_6.target.move_to(0.9 * DOWN + 4.8 * RIGHT)
		index_7.target.move_to(2.7 * DOWN + 5.6 * LEFT)
		index_8.target.move_to(2.7 * DOWN + 4.0 * LEFT)
		index_9.target.move_to(2.7 * DOWN + 2.4 * LEFT)

		self.play(
			MoveToTarget(index_0),
			MoveToTarget(index_1),
			MoveToTarget(index_2),
			MoveToTarget(index_3),
			MoveToTarget(index_4),
			MoveToTarget(index_5),
			MoveToTarget(index_6),
			MoveToTarget(index_7),
			MoveToTarget(index_8),
			MoveToTarget(index_9)
		)

	def showParentPointer(self, box):
		heapify_text = TextMobject("Heapify").move_to(2.7 * UP + 3.2 * LEFT)
		self.parent_pointer.next_to(box, UP)
		self.play(
			DrawBorderThenFill(self.parent_pointer),
			Write(heapify_text),
		)
		self.play(FadeOut(heapify_text))

	def moveParentPointer(self, box):
		self.parent_pointer.target.next_to(box, UP)
		self.play(MoveToTarget(self.parent_pointer))