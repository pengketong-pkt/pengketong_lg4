# -*- coding: utf-8 -*-
# @Time    : 2021/3/15 18:31
# @Author  : pengketong
# -*- coding: utf-8 -*-


import time

import pytest


@pytest.mark.baidu
class TestBaidu:

    @pytest.mark.parametrize('search_string, expect_string', [('iTesting', 'iTesting'), ('helloqa.com', 'iTesting')])
    def test_baidu_search(self, login, search_string, expect_string):
        driver, s, base_url = login

        driver.get(base_url + "/")

        driver.find_element_by_id("kw").send_keys(search_string)

        driver.find_element_by_id("su").click()

        time.sleep(2)

        search_results = driver.find_element_by_xpath('//*[@id="1"]/h3/a').get_attribute('innerHTML')

        print(search_results)

        assert (expect_string in search_results) is True


if __name__ == "__main__":
    pytest.main([])
