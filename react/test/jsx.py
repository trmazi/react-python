# Copyright 2013 Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import join
from react import jsx
from react.test import TEST_ROOT
from unittest import TestCase


class TestJSXTransformer(TestCase):

    def test_transform(self):
        jsx_path = join(TEST_ROOT, 'files/test.jsx')
        js_path = join(TEST_ROOT, 'files/test.js')

        with open(js_path, 'r') as js:
            self.assertEquals(
                jsx.transform(jsx_path),
                unicode(js.read()))

        malformed_path = join(TEST_ROOT, 'files/malformed.jsx')
        self.assertRaises(
            jsx.TransformError,
            lambda: jsx.transform(malformed_path))

    def test_transform_string(self):
        result = jsx.transform_string('<div />')
        self.assertEquals(result, 'React.createElement("div", null)')

    def test_transform_string_harmony(self):
        result = jsx.transform_string('var {x} = y', harmony=True)
        self.assertEquals(result, 'var $__0=  y,x=$__0.x')

    def test_transform_string_strip_types(self):
        result = jsx.transform_string('var x: Number = 1', strip_types=True)
        self.assertEquals(result, 'var x         = 1')
