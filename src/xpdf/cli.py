import typer

# from xpdf.command.app_instance import app
# from .command.version import app
from .command import watermark

# from loguru import logger

# import khelper.device
# from khelper.attm import ATTM
# from khelper.attmcase import attmcase
# from khelper.da import ios_signing, ios_teamid, ios_wda_install
# from khelper.kim import time_send
# from khelper.package import Plantform
# from khelper.pipeline import Pipeline


app = typer.Typer()


# @app.command()
# def lastest_package(
#     plantform: str = typer.Argument(..., help="'ios' or 'android'"),
#     branch: str = typer.Argument(
#         "release",
#         help="分支, 目前 keep 接口返回 develop, release, pre_develop, pre_release, pre_pre_develop, pre_pre_release",
#     ),
#     bits: int = typer.Argument(64, help="64或者32位, eg: 64"),
#     pid: int = typer.Option(1, help="产品号, 不要问这麽知道, 1 是快手的产品号, 32 是极速版产品号"),
#     keep_info: bool = typer.Option(False, help="keep_info 用于 krunner 装包和平台显示安装包信息"),
#     upload_keep_info: bool = typer.Option(True, help="向 ATTM task 上报 keep_info"),
#     tag: str = typer.Option("", help="eg: HuiduLite, Huidu"),
# ) -> None:
#     """查找最新 XX 分支包

#     eg:\n
#         khelper lastest-package ios develop\n
#         khelper lastest-package android release 32\n
#         khelper lastest-package android\n
#     """

#     p = Plantform(plantform, pid, bits, branch, tag)
#     if keep_info:
#         typer.echo(p.keep_info)
#     else:
#         typer.echo(p.latest_package_url)
#     task_id = ATTM.get_task_id()
#     logger.debug(f"task_id: {task_id}")
#     if upload_keep_info and task_id:
#         ATTM.upload_keep_info(p.keep_info)

#     exec_id = ATTM.get_exec_id()
#     logger.debug(f"exec_id: {exec_id}")
#     if upload_keep_info and exec_id:
#         ATTM.update_exec_extra(exec_id, p.keep_info_for_attm_exec_extra)


def get_version() -> str:
    from . import __version__

    return __version__


@app.command()
def version() -> None:
    typer.echo(get_version())


# @app.command()
# def sssss() -> None:
#     typer.echo(get_version())


# @app.command()
# def attm_case(
#     productid: int = typer.Option(
#         0,
#         help="默认为0,即不对product进行筛选。\
#         欲筛选出某个product,可看对应的product页面链接,当layerType=2,layerId就是productid",
#     ),
#     platform: str = typer.Option("both", help="可选择both, android, ios"),
#     day: int = typer.Option(7, help="当天前n天的稳定性数据统计,默认为7天"),
#     kim_key: str = typer.Option(...),
#     threshold: float = typer.Option(0, help="稳定性数据低于该值数值将标为红色,默认为0"),
# ) -> None:
#     """
#     获取阿童木最近n天的指定端用例执行的稳定性

#     e.g.\n
#     khelper attm-case --day 2 --kim-key {群机器人key} --platform android --threshold 0.8
#     """

#     result = attmcase(
#         productid=productid,
#         platform=platform,
#         day=day,
#         kim_key=kim_key,
#         threshold=threshold,
#     )
#     typer.echo(result)


# @app.command()
# def add_attm_result(
#     result1: str = typer.Argument(None, help="result1"),
#     result2: str = typer.Argument(None, help="result2"),
#     result3: str = typer.Argument(None, help="result3"),
# ) -> None:
#     """
#     ATTM 添加结果,可以作为任务上下游编排

#     e.g.\n
#     khelper add-attm-result "result1_foo" ["result2_bar" ["result3"]]
#     """

#     res = ATTM.add_result(result1=result1, result2=result2, result3=result3)
#     typer.echo(json.dumps(res))


# @app.command()
# def ios_certification(
#     text: str = typer.Option("wda", help="证书种类，是安装wda、newsafari、或其他软件的证书，方便直观通知"),
#     team_id: str = typer.Option(..., help="10个字符的字符串，证书团队id"),
#     serialnumber: str = typer.Option(..., help="证书对应某个包的序列号"),
#     day: int = typer.Option(10, help="提前n天通知证书到期,默认为10天"),
#     kim_key: str = typer.Option(...),
#     owner: str = typer.Option("", help="负责人邮箱前缀"),
# ) -> None:
#     """
#     ios各证书提前进行群通知

#     e.g.\n
#     khelper ios-certification --text wda --team-id FUW2ACPP --serialnumber {serialnumber} --day 2 --kim-key {群机器人key}
#     """

#     result = ios_signing(
#         text=text,
#         team_id=team_id,
#         serialnumber=serialnumber,
#         day=day,
#         kim_key=kim_key,
#         owner=owner,
#     )
#     typer.echo(result)


# @app.command()
# def ios_getteamid(
#     serial_no: str = typer.Argument(..., help="serial_no of device"),
# ) -> None:
#     """通过设备序列号查询对应的team id

#     eg:\n
#         khelper ios-getteamid xxxxxx\n
#     """
#     try:
#         result = ios_teamid(serial_no)
#     except Exception as e:
#         message = typer.style(e, fg=typer.colors.WHITE, bg=typer.colors.RED)
#         typer.echo(message, err=True)
#         raise typer.Exit(1)

#     typer.echo(result)


# @app.command()
# def ios_wdainstall(
#     serial: str = typer.Argument(..., help="serial of device"),
#     account_name: str = typer.Option("all", "--account_name", help="Optional account name"),
# ) -> None:
#     """对iOS进行wda重装

#     eg:\n
#         khelper ios-wdainstall xxxxxx\n
#     """
#     try:
#         ios_wda_install(serial=serial, account=account_name)
#     except Exception as e:
#         message = typer.style(e, fg=typer.colors.WHITE, bg=typer.colors.RED)
#         typer.echo(message, err=True)
#         raise typer.Exit(1)


# @app.command()
# def kim_markdown(
#     key: str = typer.Option(..., help="kim robot key"),
#     msg: str = typer.Option(..., help="kim message"),
#     date: str = typer.Option(..., help="目标时间, e.g.2022-11-01"),
#     delta_day: int = typer.Option(..., help="提前几天通知"),
# ) -> None:
#     """规定时间发kim群机器人通知

#     eg:\n
#         khelper kim-markdown --key xxxx --msg 中文 --date 2022-11-01 --delta-day 300  \n
#     """
#     try:
#         time_send(robot_key=key, markdown_msg=msg, date=date, delta_day=delta_day)
#     except Exception as e:
#         message = typer.style(e, fg=typer.colors.WHITE, bg=typer.colors.RED)
#         typer.echo(message, err=True)
#         raise typer.Exit(1)


# @app.command()
# def get_did(
#     serial_no: str = typer.Argument(..., help="serial_no of device"),
# ) -> None:
#     """查询设备 did

#     eg:\n
#         khelper get-did f0d3c5af\n
#     """
#     try:
#         result = khelper.device.get_did(serial_no)
#     except Exception as e:
#         message = typer.style(e, fg=typer.colors.WHITE, bg=typer.colors.RED)
#         typer.echo(message, err=True)
#         raise typer.Exit(1)

#     typer.echo(result)


# @app.command()
# def kxb_callback(
#     app_debug_url: str = typer.Argument(..., help="kxb app_debug_url"),
#     app_debug_android_test: str = typer.Argument(..., help="kxb app_debug_android_test"),
#     callback_url: Optional[str] = typer.Option(None, help="callback URL"),
#     message: Optional[str] = typer.Option(None, help="None if no error"),
# ) -> None:
#     """kxb 组件库打包 pipeline callback

#     eg:\n
#         khelper kxb_callback app_debug_url app_debug_android_test --callback-url 'URL'
#     """
#     extra_result = {}
#     extra_result["APP_DEBUG_URL"] = app_debug_url
#     extra_result["APP_DEBUG_ANDROID_TEST"] = app_debug_android_test
#     logger.debug(f"extra_result: {extra_result}")

#     res = Pipeline.callback(
#         message=message,
#         title="kxb 打包",
#         extra_result=extra_result,
#         callback_url=callback_url,
#     )
#     typer.echo(res)


# @app.command()
# def pipe_callback_error(
#     message: str = typer.Argument(..., help="error message"),
#     title: str = typer.Argument(..., help="pipeline title"),
#     callback_url: Optional[str] = typer.Option(None, help="callback URL"),
# ) -> None:
#     """组件库打包 pipeline error callback

#     eg:\n
#         khelper pipe-callback-error 'some message' 'title' --callback_url 'URL'
#     """
#     res = Pipeline.callback(message=message, title=title, extra_result={}, callback_url=callback_url)
#     typer.echo(res)


# @app.command()
# def upload_keep_version(
#     keep_version: str = typer.Argument(..., help="keep version"),
# ) -> None:
#     """上报 keep version 用于专有前端展示，只在 attm 中使用

#     eg:\n
#         khelper upload-keep-version 'keep_version'
#     """
#     ATTM.upload_keep_version_name(keep_version)


# @app.command()
# def get_attm_task_extra(
#     key: str = typer.Argument(..., help="key of ATTM extra"),
# ) -> None:
#     """获取 ATTM extra 参数

#     eg:\n
#         khelper get-attm-task-extra key
#     """
#     res = ATTM.get_extra_info(key)
#     typer.echo(res)


# @app.callback()
# def core(ctx: typer.Context, debug: bool = False) -> None:
#     if not debug:
#         logger.remove()
#         logger.add(sys.stderr, level=logging.ERROR)
#     logger.debug(ctx.invoked_subcommand)
#     sentry_sdk.capture_message(ctx.invoked_subcommand or "test")
#     sentry_sdk.flush()


# app.add_typer(add_watermark, name="add_watermark")
app.add_typer(watermark.app, name="watermark")


def main():
    # print('main begin')
    app()


if __name__ == "__main__":
    main()
