package org.primec.app.paytracker.util;

/*******************************************************************************
 * @project com.jack.paytracker - com.jack.paytracker.handler: 10/7/2025 @ 10:27 PM
 * @autor Jack Malik - Primechannel Corporation Ltd.
 *******************************************************************************/

import com.fasterxml.jackson.core.JsonParser;
import com.fasterxml.jackson.databind.DeserializationContext;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.deser.std.StdDeserializer;

import java.io.IOException;
import java.io.Serial;
import java.time.LocalDateTime;

public class LocalDateTimeDeserializer extends StdDeserializer<LocalDateTime> {

	@Serial
    private static final long serialVersionUID = 1L;

	public LocalDateTimeDeserializer() {
        super(LocalDateTime.class);
    }

    @Override
    public LocalDateTime deserialize(JsonParser parser, DeserializationContext context) throws IOException {
        JsonNode node = parser.getCodec().readTree(parser);
        String dateString = node.asText(); // Assume the date is provided as a string
        return LocalDateTime.parse(dateString); // Customize date parsing if necessary
    }
}

