/**
 * Asynchronously loads data from a data source based on the provided properties.
 * @param {IDataSourceProps} props - The properties for loading the data source.
 * @returns {Promise<IRow[]>} A Promise that resolves with an array of rows.
 */
export async function loadDataSource(props: IDataSourceProps): Promise<IRow[]> {
    // Destructure the dataSourceId from props
    const { dataSourceId } = props;

    // Create a new Promise for asynchronous operation
    return new Promise((resolve, reject) => {
        // Initialize an array to store rows
        const data = new Array<IRow>();
        
        // Define timeout duration and set an initial timer
        const TIMEOUT_DURATION = 100_000;
        let timer = setTimeout(timeout, TIMEOUT_DURATION);

        // Timeout function to reject the Promise if loading takes too long
        const timeout = () => {
            reject("timeout");
        };

        // Event listener for the 'message' event
        const onmessage = (ev: MessageEvent<MessagePayload>) => {
            // Check if the dataSourceId from the event matches the expected dataSourceId
            if (Object.is(ev.data.dataSourceId, dataSourceId)) {
                // Clear the timer and set a new one to refresh the timeout
                clearTimeout(timer);
                timer = setTimeout(timeout, TIMEOUT_DURATION);

                // Handle different actions based on the event action type
                if (ev.data.action === "postData") {
                    // Handle 'postData' action
                    handlePostData(ev.data);
                } else if (ev.data.action === "finishData") {
                    // Handle 'finishData' action
                    handleFinishData();
                }
            }
        };

        // Attach the event listener to the 'message' event
        window.addEventListener("message", onmessage);
    });
}

/**
 * Handles the 'postData' action, updating the UI and accumulating data.
 * @param {MessagePayload} eventData - The payload containing data and UI information.
 */
const handlePostData = (eventData: MessagePayload) => {
    // Update UI using common store
    commonStore.setInitModalOpen(true);
    commonStore.setInitModalInfo({
        total: eventData.total,
        curIndex: eventData.curIndex,
        title: "Loading Data",
    });

    // Accumulate data from the event payload
    for (const row of eventData.data ?? []) {
        data.push(row);
    }
};

/**
 * Handles the 'finishData' action, removing the event listener and resolving the Promise.
 */
const handleFinishData = () => {
    // Remove the event listener to prevent further handling
    window.removeEventListener("message", onmessage);

    // Resolve the Promise with the accumulated data
    resolve(data);
};
