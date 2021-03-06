# coding: utf-8

"""
    Pesaway Pesamoni API Documentation
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pesamoni_python.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def transactions_post(self, method, amount, **kwargs):  # noqa: E501
        """transactions_post  # noqa: E501

        Below are parameters and their respective expected responses. In order to try out the service, simply click Try it out.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transactions_post(method, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str method: Enter a request method. To check for request methods <a href=''>click here</a> (required)
        :param str amount: Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p> (required)
        :param str mobile: Enter the mobile number you would like to execute the above method in format 256.... or 254...<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, senderid, sendsms, sendairtime</b></p>
        :param str holdername: Enter name of payer for Visa/MasterCard transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str cardnumber: Enter the Visa/MasterCard cardnumber<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str cvv: Enter the Visa/MasterCard cvv<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str exp: Enter the Visa/MasterCard expiry date in the format MM/YYYY e.g 07/2030<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str currency: Enter the currency you intend to make the transaction for Visa/MasterCard based transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str account: Enter the Pesamoni account you would like to use for this transaction<p style=\"color:red\">This method applies for request method <b>paybills</b></p>
        :param str reference: Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p>
        :param str genericmsg: Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
        :param str token: Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
        :param str bouquet: Enter the bouquet or package you would like to pay for<p style=\"color:red\">This method applies for request methods <b>paybills</b></p>
        :param str payoption: Enter your prefered payment option<p style=\"color:red\">This method applies for request methods <b>paybills</b></p>
        :param str meternumber: Enter the meter number for the intended payment<p style=\"color:red\">This method applies for request methods <b>paybills</b></p>
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.transactions_post_with_http_info(method, amount, **kwargs)  # noqa: E501
        else:
            (data) = self.transactions_post_with_http_info(method, amount, **kwargs)  # noqa: E501
            return data

    def transactions_post_with_http_info(self, method, amount, **kwargs):  # noqa: E501
        """transactions_post  # noqa: E501

        Below are parameters and their respective expected responses. In order to try out the service, simply click Try it out.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.transactions_post_with_http_info(method, amount, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str method: Enter a request method. To check for request methods <a href=''>click here</a> (required)
        :param str amount: Enter the amount you would like to request for. <p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, acsendbank, pesab2c, sendairtime, cardaccept</b></p> (required)
        :param str mobile: Enter the mobile number you would like to execute the above method in format 256.... or 254...<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, senderid, sendsms, sendairtime</b></p>
        :param str holdername: Enter name of payer for Visa/MasterCard transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str cardnumber: Enter the Visa/MasterCard cardnumber<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str cvv: Enter the Visa/MasterCard cvv<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str exp: Enter the Visa/MasterCard expiry date in the format MM/YYYY e.g 07/2030<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str currency: Enter the currency you intend to make the transaction for Visa/MasterCard based transactions<p style=\"color:red\">This method applies for request method <b>cardaccept</b></p>
        :param str account: Enter the Pesamoni account you would like to use for this transaction<p style=\"color:red\">This method applies for request method <b>paybills</b></p>
        :param str reference: Enter your user generated transaction reference<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, transactionstatus, sendairtime, pesab2c, sendsms, cardaccept</b></p>
        :param str genericmsg: Enter your user generated generic message for the requested transaction<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
        :param str token: Enter your user generated token for the above mentioned method<p style=\"color:red\">This method applies for request methods <b>acreceive, acreceivekeac, acsend, acsendkeac, sendsms, sendairtime, pesab2c, sendsms, cardaccept</b></p>
        :param str bouquet: Enter the bouquet or package you would like to pay for<p style=\"color:red\">This method applies for request methods <b>paybills</b></p>
        :param str payoption: Enter your prefered payment option<p style=\"color:red\">This method applies for request methods <b>paybills</b></p>
        :param str meternumber: Enter the meter number for the intended payment<p style=\"color:red\">This method applies for request methods <b>paybills</b></p>
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['method', 'amount', 'mobile', 'holdername', 'cardnumber', 'cvv', 'exp', 'currency', 'account', 'reference', 'genericmsg', 'token', 'bouquet', 'payoption', 'meternumber']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method transactions_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'method' is set
        if ('method' not in params or
                params['method'] is None):
            raise ValueError("Missing the required parameter `method` when calling `transactions_post`")  # noqa: E501
        
        
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'method' in params:
            query_params.append(('method', params['method']))  # noqa: E501
        if 'amount' in params:
            query_params.append(('amount', params['amount']))  # noqa: E501
        if 'mobile' in params:
            query_params.append(('mobile', params['mobile']))  # noqa: E501
        if 'holdername' in params:
            query_params.append(('holdername', params['holdername']))  # noqa: E501
        if 'cardnumber' in params:
            query_params.append(('cardnumber', params['cardnumber']))  # noqa: E501
        if 'cvv' in params:
            query_params.append(('cvv', params['cvv']))  # noqa: E501
        if 'exp' in params:
            query_params.append(('exp', params['exp']))  # noqa: E501
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501
        if 'account' in params:
            query_params.append(('account', params['account']))  # noqa: E501
        if 'reference' in params:
            query_params.append(('reference', params['reference']))  # noqa: E501
        if 'genericmsg' in params:
            query_params.append(('genericmsg', params['genericmsg']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501
        if 'bouquet' in params:
            query_params.append(('bouquet', params['bouquet']))  # noqa: E501
        if 'payoption' in params:
            query_params.append(('payoption', params['payoption']))  # noqa: E501
        if 'meternumber' in params:
            query_params.append(('meternumber', params['meternumber']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apipassword', 'apiusername']  # noqa: E501

        return self.api_client.call_api(
            '/transactions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
