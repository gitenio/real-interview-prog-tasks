package org.primec.app.paytracker;

/*******************************************************************************
 * @project PayTracker - com.jack.paytracker: 10/9/2025 @ 11:15 AM
 * @autor Jack Malik - Primechannel Corporation Ltd.
 *******************************************************************************/

import org.primec.app.paytracker.db.DbConnectionPool;
import org.junit.jupiter.api.*;

import org.mockito.Mock;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class PayTrackerTests {

    private TestInfo testInfo;
    private final static Logger logger = LoggerFactory.getLogger(PayTrackerTests.class);

    @Mock
    private DbConnectionPool connectionPool;

    @BeforeAll
    static void setup() {

    }

    @BeforeEach
    void init(TestInfo testInfo) {
        this.testInfo = testInfo;
    }

    @Test
    @DisplayName("Testing PayTracker cache building")
    void testPayTrackerBuildCacheMethod() {
        return;
    }
}

