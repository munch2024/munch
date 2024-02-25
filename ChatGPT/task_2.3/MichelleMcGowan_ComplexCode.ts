
export async function loadDataSource(props: IDataSourceProps): Promise<IRow[]> {
    const { dataSourceId } = props;

    return new Promise((resolve, reject) => {
        const data = new Array<IRow>();
        const timeout = () => {
            reject("timeout");
        };
        let timer = setTimeout(timeout, 100_000);
        const onmessage = (ev: MessageEvent<MessagePayload>) => {
            try {
                if (ev.data.dataSourceId === dataSourceId) {
                    clearTimeout(timer);
                    timer = setTimeout(timeout, 100_000);
                    if (ev.data.action === "postData") {
                        commonStore.setInitModalOpen(true);
                        commonStore.setInitModalInfo({
                            total: ev.data.total,
                            curIndex: ev.data.curIndex,
                            title: "Loading Data",
                        });
                        data.push(...(ev.data.data ?? []));
                    } else if (ev.data.action === "finishData") {
                        window.removeEventListener("message", onmessage);
                        resolve(data);
                    }
                }
            } catch (err) {
                reject({ message: "handler", error: err });
            }
        };
        window.addEventListener("message", onmessage);
    });
}
