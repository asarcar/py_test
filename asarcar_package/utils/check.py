#!/usr/bin/python3

# Copyright 2025 Arijit Sarcar.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Generic check functions

# Check if the value is None
def check_not_none(value) -> None:
  assert value is not None, "Value is None"

# Check if the value is expected
def check_value(value, expected) -> None:
  assert value == expected, f"Value is {value}, but expected {expected}"

# Check if the value is greater than the expected value
def check_greater(value, expected) -> None:
  assert value > expected, f"Value is {value}, but expected greater than {expected}"

# Check if the value is lesser than the expected value
def check_lesser(value, expected) -> None:
  assert value < expected, f"Value is {value}, but expected lesser than {expected}"

# Check if the value is in the expected range(low, high) or [elem1, elem2, ...]
def check_in_range(value, expected) -> None:
  assert value in expected, f"Value is {value}, but expected in {expected}"

# check type is int
def check_type_int(value: int) -> None:
  assert isinstance(value, int), f"Value is {value}, but expected int"

# check type is string
def check_type_string(value: str) -> None:
  assert isinstance(value, str), f"Value is {value}, but expected string"

# check type is list
def check_type_list(value: list) -> None:
  assert isinstance(value, list), f"Value is {value}, but expected list"

# check type is dict
def check_type_dict(value: dict) -> None:
  assert isinstance(value, dict), f"Value is {value}, but expected dict"

# check type is set
def check_type_set(value: set) -> None:
  assert isinstance(value, set), f"Value is {value}, but expected set"

# check type is tuple
def check_type_tuple(value: tuple) -> None:
  assert isinstance(value, tuple), f"Value is {value}, but expected tuple"

# check type is bool
def check_type_bool(value: bool) -> None:
  assert isinstance(value, bool), f"Value is {value}, but expected bool"

# check type is float
def check_type_float(value: float) -> None:
  assert isinstance(value, float), f"Value is {value}, but expected float"

# check type is None
def check_type_none(value: None) -> None:
  assert value is None, f"Value is {value}, but expected None"

# check type is bytes
def check_type_bytes(value: bytes) -> None:
  assert isinstance(value, bytes), f"Value is {value}, but expected bytes"

# check type is bytearray
def check_type_bytearray(value: bytearray) -> None:
  assert isinstance(value, bytearray), f"Value is {value}, but expected bytearray"

# check type is memoryview
def check_type_memoryview(value: memoryview) -> None:
  assert isinstance(value, memoryview), f"Value is {value}, but expected memoryview"

# check type is complex
def check_type_complex(value: complex) -> None:
  assert isinstance(value, complex), f"Value is {value}, but expected complex"

# check type is object
def check_type_object(value: object) -> None:
  assert isinstance(value, object), f"Value is {value}, but expected object"

# check type is function
def check_type_function(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected function"

# check type is method
def check_type_method(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected method"

# check type is generator
def check_type_generator(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected generator"

# check type is coroutine
def check_type_coroutine(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected coroutine"

# check type is async function
def check_type_async_function(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected async function"

# check type is async generator
def check_type_async_generator(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected async generator"

# check type is async coroutine
def check_type_async_coroutine(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected async coroutine"

# check type is async method
def check_type_async_method(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected async method"

# check type is async function
def check_type_async_function(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected async function"

# check type is async generator
def check_type_async_generator(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected async generator"

# check type is async coroutine
def check_type_async_coroutine(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected async coroutine"

# check type is async method
def check_type_async_method(value: callable) -> None:
  assert callable(value), f"Value is {value}, but expected async method"


