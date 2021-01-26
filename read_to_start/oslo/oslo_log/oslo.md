https://docs.openstack.org/oslo.log/latest/user/usage.html#in-an-application  
使用标准的python ***log***库  

    import logging
    LOG = logging.getLogger(__name__)

    # Define a default handler at INFO logging level
    logging.basicConfig(level=logging.INFO)
    
    LOG.info("Python Standard Logging")
    LOG.warning("Python Standard Logging")
    LOG.error("Python Standard Logging")
    
使用oslo.log库

    from oslo_config import cfg
    from oslo_log import log as logging
    
    LOG = logging.getLogger(__name__)
    CONF = cfg.CONF
    DOMAIN = "mall"
    
    logging.register_options(CONF)
    logging.setup(CONF, DOMAIN)
    
    # Oslo Logging uses INFO as default
    LOG.info("Oslo Logging")
    LOG.warning("Oslo Logging")
    LOG.error("Oslo Logging")

往日志中添加上下文

    LOG.info("Welcome to Oslo Logging")
    LOG.info("Without context")
    context.RequestContext(user='6ce90b4d',
                           tenant='d6134462',
                           domain='a6b9360e')
    LOG.info("With context")
    
> 输出结果如下

    2016-01-14 20:04:34.562 11266 INFO __main__ [-] Welcome to Oslo Logging
    2016-01-14 20:04:34.563 11266 INFO __main__ [-] Without context
    2016-01-14 20:04:34.563 11266 INFO __main__ [req-bbc837a6-be80-4eb2-8ca3-53043a93b78d 6ce90b4d d6134462 a6b9360e - -] With context