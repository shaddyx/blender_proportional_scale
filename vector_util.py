
import mathutils


def xy_vect(vect: mathutils.Vector) -> mathutils.Vector:
    return mathutils.Vector((vect.x, vect.y))


def prolong_vector(from_vector: mathutils.Vector, to_vector: mathutils.Vector, size: float) -> mathutils.Vector:
    vect_delta: mathutils.Vector = xy_vect(to_vector) - xy_vect(from_vector)
    scale = (vect_delta.length + size) / vect_delta.length
    return xy_vect(from_vector) + (vect_delta * scale)


if __name__ == "__main__":
    res = prolong_vector(mathutils.Vector((0, 0, 0)), mathutils.Vector((1, 1, 1)), 6)
    assert res.length == 7.414213253373814, res.length
    # res = prolong_vector(mathutils.Vector((1, 1, 1)), mathutils.Vector((2, 2, 2)), 5)
    # print((res - mathutils.Vector((1, 1))).length)
    # print(res)
    res = prolong_vector(mathutils.Vector((0, 0, 0)), mathutils.Vector((2, 2, 2)), 0.3)
    print(res.length)
    print(res)