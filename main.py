# Copyright (c) 2021 Amy Grace.
# 
# This file is part of shsh2-saver.
# See https://github.com/00p513-dev/shsh2-saver for further info.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json, requests

def main():
	headers = {'Content-type': 'application/json'}
	with open('data.json') as json_file:
		data = json.load(json_file)
		for i in data:
			current = data[i][0]
			response = requests.post('https://tsssaver.1conan.com/v2/api/save.php', json=current, headers=headers)
			print(response.status_code)

if __name__ == "__main__":
	main()
